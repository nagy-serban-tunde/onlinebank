// a register endpoint eleresre itt tortenhet meg

import Api from './Api'
import { strict } from 'assert';

export default {
    register: (auth_data) => {
        return Api().post('/register', auth_data);
    },
    account: async (id) => {
        let page = '/user/' + String(id);
        return (await Api().get(page)).data;
    },
    getcard: async (id) => {
        let page = '/cards/' + String(id);
        return (await Api().get(page)).data;
    },
    getdeposit: async (id) => {
        let page = '/deposit/' + String(id);
        return (await Api().get(page)).data;
    },
    statisticIncome: async (id) => {
        let page = '/statisticIncome/' + String(id);
        return (await Api().get(page)).data;
    },
    statisticExpense: async (id) => {
        let page = '/statisticExpense/' + String(id);
        return (await Api().get(page)).data;
    },
    statisticExchangeNumber: async (id) => {
        let page = '/statisticExchangeNumber/' + String(id);
        return (await Api().get(page)).data;
    },
    statisticValuta: async (valuta) => {
        let page = '/statisticValuta/' + valuta;
        return (await Api().get(page)).data;
    },
    verification: (verif_data) => {
        return Api().post('/verification', verif_data);
    },
    changedeposit: (deposit) => {
        return Api().post('/changedeposit', deposit);
    },
    changepassword: (new_password) => {
        return Api().post('/changepassword', new_password);
    },
    gettransactiontypes: async () => {
        let page = '/transactiontypes';
        return (await Api().get(page)).data;
    },
    sendtransaction: (transaction) => {
        return Api().post('/sendtransaction', transaction);
    },
  
}