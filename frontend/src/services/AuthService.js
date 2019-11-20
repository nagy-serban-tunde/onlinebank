// a register endpoint eleresre itt tortenhet meg

import Api from './Api'

export default {
    register: (auth_data) => {
        return Api().post('register', auth_data);
    }
}