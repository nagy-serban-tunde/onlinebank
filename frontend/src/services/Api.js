// Ez lesz hanszalva arra, hogy az endpointokat elerjuk a frontednrol
import axios from 'axios'

export default () => {
    return axios.create({
        baseURL:'http://localhost:8081/'
    })
}