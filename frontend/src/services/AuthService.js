// a register endpoint eleresre itt tortenhet meg

import Api from './Api'
import { strict } from 'assert';

export default {
    register: (auth_data) => {
        return Api().post('register', auth_data);
    },
    account: async (id) => {
        let page = '/user/' + String(id);
        return (await Api().get(page)).data;
    },
    DepositRonInfo: async (id) => {
        let page = '/depositRON/' + String(id);
        return (await Api().get(page)).data;
    },
    verification: (verif_data) => {
        return Api().post('verification', verif_data);
    },
    changedeposit: (new_deposit) => {
        return Api().post('changedeposit', new_deposit);
    },
    changepassword: (new_password) => {
        return Api().post('changepassword', new_password);
    },
}