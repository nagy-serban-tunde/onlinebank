import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import jwt from 'jsonwebtoken'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        user : JSON.parse(localStorage.getItem('user')) || {}
    },
    mutations: {
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, {token, user}){
            state.status = 'success'
            state.token = token
            state.user = user
        },
        auth_error(state){
            state.status = 'error'
        },
        admin_error(state){
            state.status = 'admin_error'
            state.token = ''
            state.user = {}
        },
        logout(state){
            state.status = ''
            state.token = ''
            state.user = {}
        },
        list_request(state){
            state.status = 'loading';
        }
    },
    actions: {
        login({commit}, myUser){
            return new Promise((resolve, reject) => {
              commit('auth_request')
              axios.get('static/user.json')
              .then(resp => {
                const user = resp.data.find(u=>{
                    return u.username===myUser.username
                })
                if(!user){
                    commit('auth_error')
                    return
                }
                if(user.username!=myUser.username){
                    commit('auth_error')
                    return
                }
                if(user.password!=myUser.password){
                    commit('auth_error')
                    return
                }
                const token = jwt.sign({ id: user.id },'secret', {expiresIn: 30 // expires in 24 hours
                });
                localStorage.setItem('token', token)
                localStorage.setItem('user',JSON.stringify(user))
                console.log(user.name + " " +user.avatar)
                axios.defaults.headers.common['Authorization'] = token
                commit('auth_success', {token, user})
                resolve(resp)
              })
              .catch(err => {
                commit('auth_error')
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                reject(err)
              })
            })
        },
        logout({commit}){
            return new Promise((resolve, reject) => {
              commit('logout')
              localStorage.removeItem('token')
              localStorage.removeItem('user')
              delete axios.defaults.headers.common['Authorization']
              resolve()
            })
        },
        errorNotAdmin({commit}){
            commit('admin_error')
        }
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status
    }
})