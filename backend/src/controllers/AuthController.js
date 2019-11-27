module.exports = {
    register(req, res) {
        var sql = `INSERT INTO user (full_name, birth_date, profile_picture, created_at, gender, password, email_addres, phone_number, deposit) VALUES ( "${req.body.name}", '1998-04-22', 'cucc', CURDATE(), 'M', "${req.body.password}", 'zb@yahoo.ro', '0751186829', 0)`;
        connection.query(sql, function (err, result) {
            if (err) throw err;
            var resmsg = `User ${req.body.name} registered!`;
            res.send({
                message: resmsg
            })
            console.log(resmsg);
        });
        console.log(req.body);
    }
}
