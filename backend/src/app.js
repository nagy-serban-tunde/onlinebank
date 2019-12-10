//python import
const child_process = require('child_process')

// modulok importalasa
const express = require('express');
// bodyParser segit feldolgozni json fileokat konnyen
const bodyParser = require('body-parser');
const morgan = require('morgan');
const cors = require('cors');
const mysql = require('mysql');
const config = require('./config/config');

// felepeti az express servert
const app = express();
// combined-al megjelenit meta-informaciokat a reqestet feladorol
app.use(morgan('combined'));
app.use(bodyParser.json());
app.use(cors());

/*Fobb express requestekek: get, post, put, patch, delete, stb... */
const connection = mysql.createConnection({
    host: config.db.host,
    user: config.db.user,
    password: config.db.password,
    database: config.db.database,
});


connection.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
});

function formatDate(date) {
    var monthNames = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun", "Jul",
        "Aug", "Sep", "Oct",
        "Nov", "Dec"
    ];

    var day = date.getDate();
    var monthIndex = date.getMonth();
    var year = date.getFullYear();

    return day + ' ' + monthNames[monthIndex] + ', ' + year;
}

app.get('/transactionlist/:id', async (req, res) => {
    const sqlgetalltransactions = `SELECT * FROM ( SELECT t.user_id "user_id", t.date "date", t.type "attitude", i.amount "amount", i.comment "comment", ty.name "name", ty.icon "icon" FROM transactions t , income i, types_ ty where i.transaction_id = t.id and ty.id = i.type and user_id = '${req.params.id}' UNION SELECT t.user_id "user_id", t.date "date", t.type "attitude", e.amount "amount", e.comment "comment", ty.name "name", ty.icon "icon" FROM transactions t , expense e, types_ ty where e.transaction_id = t.id and ty.id = e.type and t.user_id = '${req.params.id}') A ORDER BY A.date DESC`
    connection.query(sqlgetalltransactions, function (err, result) {
        var transactionList = [];
        for (i in result) {
            var date = formatDate(result[i].date)
            var type = ""
            var sign = ""
            if (result[i].attitude == "income") {
                type = "green--text"
                sign = "+"
            } else {
                type = "red--text"
                sign = "-"
            }
            transactionList.push({
                id: i,
                name: result[i].name,
                icon: result[i].icon,
                amount: result[i].amount,
                date: date,
                type: type,
                sign: sign,
                attitude: result[i].attitude,
                comment: result[i].comment
            });
        }
        res.send(transactionList);
    })
})

const insertTransaction = (req) => {
    return new Promise((resolve, reject) => {
        var sqlinserttransaction = `INSERT INTO transactions ( user_id, date, type) VALUES ('${req.body.id}', CURRENT_TIMESTAMP(),'${req.body.type}')`
        connection.query(sqlinserttransaction, function (err, result) {
            if (err) { reject(err) }
            else { resolve(result) }
            const transaction_id = result;
            if (req.body.type == "income") {
                var sqlinsertexpense = `INSERT INTO ${req.body.type} (transaction_id, amount, type, comment) VALUES ('${transaction_id.insertId}', '${req.body.amount}', '1' , '${req.body.comment}')`
                connection.query(sqlinsertexpense, function (err, result) {
                    if (err) { reject(err) }
                    else { resolve(result) }
                })
            } else {
                var sqlgettypeid = `SELECT id FROM types_ WHERE name = '${req.body.category}'`
                connection.query(sqlgettypeid, function (err, result) {
                    if (err) { reject(err) }
                    else { resolve(result) }
                    const typeid = result[0].id
                    var sqlinsertexpense = `INSERT INTO ${req.body.type} (transaction_id, amount, type, comment) VALUES ('${transaction_id.insertId}', '${req.body.amount}','${typeid}','${req.body.comment}')`
                    connection.query(sqlinsertexpense, function (err, result) {
                        if (err) { reject(err) }
                        else { resolve(result) }
                    })
                })

            }
        })
    })
}

app.post('/sendtransaction', async (req, res) => {
    transactionTypes = await insertTransaction(req).then(
        function (result) {
            res.send({
                message: 'Transaction added!'
            })
            console.log('Transaction added!')
        },
        function (error) {
            res.send({
                error: 'Invalid transaction!'
            })
            console.log('Invalid transaction!');

        }
    );
})

const getTransactionTypes = () => {
    return new Promise((resolve, reject) => {
        connection.query(`CREATE TABLE temp_tbl AS SELECT * FROM types_`, function (error, result) {
            connection.query(`DELETE FROM temp_tbl WHERE name = 'Income';`, function (error, result) {
                connection.query(`SELECT * from temp_tbl`, function (err, result) {
                    const response = result
                    connection.query(`DROP TABLE temp_tbl`, function (error, result) {
                        if (err) { reject(err) }
                        else { resolve(response) }
                        console.log(response);
                    })
                });
            });
        })
    });
}
app.get('/transactiontypes', async (req, res) => {
    transactionTypes = await getTransactionTypes().catch(err => console.error(err))
    res.send(transactionTypes);
})

app.post('/verification', function (req, res) {
    var sql = `SELECT id from user where (username = "${req.body.name}" && password="${req.body.password}")`;
    connection.query(sql, function (err, result) {
        console.log(result[0]);
        if (!result[0]) {
            res.send({
                error: 'Wrong username or password!'
            })
            console.log('Wrong username or password!');
            return;
        } else {

            res.send({
                message: `${result[0].id}`
            })
            console.log(`User ${req.body.name} logged in!`);
        }
    });
});

app.post('/register', function (req, res) {
    var sqlinsertuser = `INSERT INTO user (username, last_name ,first_name, birth_date, profile_picture, created_at, gender, password, email_addres, phone_number) VALUES ( "${req.body.name}" , "${req.body.lastname}","${req.body.firstname}","${req.body.birth_date}", "https://eu.ui-avatars.com/api/?background=fff&color=4caf50&bold=true&name=${req.body.firstname}+${req.body.lastname}", CURRENT_TIMESTAMP(), "${req.body.gender}", "${req.body.password}", "${req.body.email}", "${req.body.phonenumber}")`;
    connection.query(sqlinsertuser, function (err, result) {
        if (err) {
            res.send({
                error: 'Registration rejected! User data already in use!'
            })
            console.log('Registration rejected! User data already in use!');
            return;
        } else {


            var sqlgetuserid = `SELECT id from user where username = "${req.body.name}"`
            connection.query(sqlgetuserid, function (err, result) {
                var sqlinsertdeposit = `INSERT INTO deposit (user_id) VALUES ('${result[0].id}');`
                connection.query(sqlinsertdeposit, function (err, result) {
                    if (err) {
                        console.log(err);
                        res.send({
                            error: 'Registration rejected! Deposit creation failed!'
                        })
                        console.log('Registration rejected! Deposit creation failed!');
                        return;
                    } else {
                        res.send({
                            message: `User ${req.body.name} registered! Have fun!`
                        })
                        console.log(`User ${req.body.name} registered! Have fun!`);
                    }
                });
            });
        }
    });
});

app.post('/changedeposit', function (req, res) {
    var sql = `UPDATE deposit SET ${req.body.currency} = "${req.body.new_deposit}" WHERE user_id="${req.body.id}"`
    connection.query(sql, function (err) {
        if (err) {
            res.send({
                error: 'Deposit update error!'
            })
        } else {
            res.send({
                message: "Successful deposit update!"
            })
        }
    });

});

app.post('/changepassword', function (req, res) {
    var sql = `UPDATE user SET password = "${req.body.new_password}" WHERE id="${req.body.id}"`;
    connection.query(sql, function (err) {
        if (err) {
            res.send({
                error: 'Password change error!'
            })
        } else {
            res.send({
                message: "Successful password update"
            })
        }
    })
});

const getDeposit = (id) => {
    return new Promise((resolve, reject) => {
        connection.query(`SELECT ron, gbp, usd, eur FROM deposit where user_id = "${id}"`, function (error, results, fields) {
            if (error) { reject(error) }
            else { resolve(results[0]) }
            console.log(results[0]);
        });
    })
}

app.get('/cards/:id', async (req, res) => {
    amounts = await getDeposit(req.params.id).catch(err => console.error(err))
    var deposit = [
        {
            currency: "RON",
            amount: amounts.ron,
            sign: "",
            icon: "RON",
            from_curreny: "RON",
            exchange: "4.29",
            notification: false
        },
        {
            currency: "Euro",
            amount: amounts.eur,
            sign: "€",
            icon: "fas fa-euro-sign",
            from_curreny: "RON",
            exchange: "4.76",
            notification: false
        },
        {
            currency: "GBP",
            amount: amounts.gbp,
            sign: "£",
            icon: "fas fa-pound-sign",
            from_curreny: "RON",
            exchange: "5.50",
            notification: true
        },
        {
            currency: "USD",
            amount: amounts.usd,
            sign: "$",
            icon: "fas fa-dollar-sign",
            from_curreny: "RON",
            exchange: "4.29",
            notification: true
        }
    ];
    res.send(deposit);
})

app.get('/deposit/:id', async (req, res) => {
    deposit = await getDeposit(req.params.id).catch(err => console.error(err))
    console.log(deposit);
    res.send(deposit);
})


const getUserInfo = (id) => {
    return new Promise((resolve, reject) => {
        connection.query(`SELECT * from user where id = "${id}"`, function (error, results, fields) {
            if (error) { reject(error) }
            else { resolve(results[0]) }
            console.log(results[0]);
        });
    })
}
app.get('/user/:id', async (req, res) => {
    user = await getUserInfo(req.params.id).catch(err => console.error(err))
    user.birth_date = formatDate(user.birth_date);
    user.created_at = formatDate(user.created_at);
    res.send(user);
});

app.get('/statisticIncome/:id', async (req, res) => {
    sql = `SELECT amount,date FROM transactions t join income i on t.id = i.transaction_id where date BETWEEN NOW() - INTERVAL 30 DAY AND NOW() and user_id = "${req.params.id}";`
    connection.query(sql, function (err, result) {
        if (err) {
            res.send({
                error: 'Wrong statisticIncome'
            })
        } else {
            for (let index = 0; index < result.length; index++) {
                result[index].date = result[index].date.getTime();
            }
            res.send(result);
        }
    });
});

app.get('/statisticExpense/:id', async (req, res) => {
    sql = `select amount,date from transactions t join expense e on t.id = e.transaction_id where date BETWEEN NOW() - INTERVAL 30 DAY AND NOW() and user_id = "${req.params.id}";`
    connection.query(sql, function (err, result) {
        if (err) {
            res.send({
                error: 'Wrong statisticExpense'
            })
        } else {
            for (let index = 0; index < result.length; index++) {
                result[index].date = result[index].date.getTime();
            }
            res.send(result);
        }
    });
});

app.get('/statisticExchangeNumber/:id', async (req, res) => {
    sql = `select count(*) as number, date from exchange  where date BETWEEN NOW() - INTERVAL 30 DAY AND NOW() and user_id = "${req.params.id}" group by date;`
    connection.query(sql, function (err, result) {
        console.log(result);
        if (err) {
            res.send({
                error: "Wrong statisticExchangeNumber"
            })
        } else {
            for (let index = 0; index < result.length; index++) {
                result[index].date = result[index].date.getTime();
            }
            res.send(result);
        }
    });
});

app.get('/statisticValuta/:valuta', async (req, res) => {
    sql = `select web_address,currency,purchase_price from valuta`;
    connection.query(sql, function (err, result) {
        if (err) {
            error: 'Wrong getvaluta'
        } else {
            res.send(result);
        }
    });
});

app.get('/', (req, res) => {
    console.log('Someone connected!');
    res.send({ message: 'Hello bello te lo' });
});

//require('./routes')(app)

app.listen(config.port, function () {
    console.log(`Server is listening on port ${config.port}`);
});

function python_run() {
    const runscript = child_process.exec("python ..\\datacollector\\main.py", { timeout: 10 * 1000 })
    runscript.stdout.on('data', d => console.log(d))
    runscript.on("error", err => console.log(err))
    runscript.on("exit", () => {
        console.log("Python code runed")
    })
}
python_run();
setInterval(() => python_run(), 50 * 60 * 1000);
