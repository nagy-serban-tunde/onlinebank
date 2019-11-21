<<template>
    <div id="app">
  <v-app id="inspire" style=" background-position: center;  background-size: cover; background-repeat: no-repeat;;background-image:url('https://wallpaperaccess.com/full/222359.jpg')">
            <v-card style="border-radius:7px" max-width="400" elevation="10" outlined dark  class="ma-auto">
              <v-toolbar flat color="green" dark>
                <v-card-title>Login</v-card-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-container fluid grid-list-lg class="pt-3">
                <v-layout row wrap>
                  <v-flex>
                    
                    <v-text-field
                     class="mx-5"
                      type="name" name="name" v-model="name" placeholder="name"
                      label="Username"
                      color="green"
                      prepend-icon="fas fa-user"
                      @click="textfieldSelected=true"
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12>
                 
            <v-text-field
                  type="password" name="password" v-model="password" placeholder="password"
           class="mx-5"
        label="Password"
        color="green"
        :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
        :type="show ? 'text' : 'password'"
        counter="24"
        @click:append="show = !show"
        :rules="[rules.required, rules.min]"
        prepend-icon="fas fa-lock"  
      />
                  </v-flex>
                  <v-layout justify-center align-center>
                    <v-btn outlined class="mt-3 mb-5" color="success" text @click="register">Register</v-btn>
                  </v-layout>
                </v-layout>
              </v-container>
            </v-card>
  </v-app>
</div>
</template>

<script>
import AuthRequest from "@/services/AuthService";

export default {
  name: "Register",
  data() {
    return {
      name: "",
      password: "",
      show: false,
      rules: {
        required: value => !!value || "Password is equired",
        min: v => v.length >= 8 || "Min 8 characters"
      }
    };
  },
  methods: {
    async register() {
      const response = await AuthRequest.register({
        name: this.name,
        password: this.password
      });
      console.log(response.data);
    }
  }
};
</script>

<style></style>