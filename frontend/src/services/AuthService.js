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
    verification: (verif_data) => {
        return Api().post('verification', verif_data);
    },
}