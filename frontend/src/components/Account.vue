<template>
  <div>
    <v-card dark>
      <v-card-title primary-title class="justify-center">
        <v-subheader class="display-1 white--text">Personal Data</v-subheader>
      </v-card-title>

      <v-list-item class="justify-space-around">
        <v-list-item-icon class="mt-5 pt-5">
          <v-icon class="fas fa-portrait"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Picture</v-list-item>
        <v-list-item class="mr-5 pr-5">
          <v-avatar size="100">
            <v-img :src = profile_picture ></v-img>
          </v-avatar>
        </v-list-item>
      </v-list-item>

      <v-divider class="mx-5" ></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="far fa-user"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Username</v-list-item>
        <v-list-item class="subtitle-1"> {{ full_name }} </v-list-item>
      </v-list-item>

      <v-divider class="mx-5"></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="far fa-clock"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Birth date</v-list-item>
        <v-list-item class="subtitle-1" > {{ birth_date }} </v-list-item>
      </v-list-item>

      <v-divider class="mx-5"></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="fas fa-venus-mars"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Gender</v-list-item>
        <v-list-item class="subtitle-1" > {{ gender }} </v-list-item>
      </v-list-item>

      <v-divider class="mx-5"></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="fas fa-unlock-alt"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Password</v-list-item>
        <v-list-item class="subtitle-1">{{ characters }}
          <v-list-item class ="ml-5 pl-5">
            <change-password></change-password>
          </v-list-item>
        </v-list-item>
      </v-list-item>

      <v-divider class="mx-5"></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="fas fa-calendar-check"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Data_accession</v-list-item>
        <v-list-item class="subtitle-1" > {{ created_at }} </v-list-item>
      </v-list-item>
    </v-card>

    <v-card dark class="mt-5">
      <v-card-title primary-title class="justify-center">
        <v-subheader class="display-1 white--text">Connection Data</v-subheader>
      </v-card-title>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="far fa-envelope"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Email Address</v-list-item>
        <v-list-item class="subtitle-1" > {{ email_addres }} </v-list-item>
      </v-list-item>

      <v-divider class="mx-5"></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="fas fa-mobile-alt"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Telephone Number</v-list-item>
        <v-list-item class="subtitle-1" > {{ phone_number }} </v-list-item>
      </v-list-item>
      <v-divider class="mx-5"></v-divider>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="fas fa-comments-dollar"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Deposit</v-list-item>
        <v-list-item class="subtitle-1 ">{{ deposit }} RON 
          <v-layout class ="ml-5 pl-5">
            <exchange-card-dialog :currency="'RON'" />
          </v-layout>
        </v-list-item>
      </v-list-item>

    </v-card>
  </div>
</template>

<script>
import ExchangeCardDialog from "./fittings/ExchangeCardDialog";
import ChangePassword from "./fittings/ChangePasswordDialog";
import AuthRequest from "@/services/AuthService";

export default {
  name: "Account",
  components: { ExchangeCardDialog , ChangePassword},
  data() {
    isMobile: false;
    this.user();
    return {
      password_other: "",
      profile_picture: "",
      full_name: "",
      birth_date: "",
      gender: "",
      password: "",
      created_at: "",
      email_addres: "",
      phone_number: "",
      deposit: "",
    };

  },

  beforeDestroy() {
    if (typeof window !== "undifined") {
      window.removeEventListener("resize", this.onResize, { passive: true });
    }
  },

  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
  },
  computed: {
    characters : function(){
      for (let index = 0; index < this.password.length; index++) {
        this.password_other = this.password_other + "*";
      }
      return this.password_other;
    },
  },

  methods: {
    async user (){
      const response = await AuthRequest.account(2);
      this.profile_picture = response.profile_picture;
      this.full_name = response.full_name;
      this.birth_date = response.birth_date;
      this.gender = response.gender;
      this.password = response.password;
      this.created_at = response.created_at;
      this.email_addres = response.email_addres;
      this.phone_number = response.phone_number;
      this.deposit = response.deposit;
    },
    
    onResize() {
      this.isMobile = window.innerWidth < 600;
    }
  },
};
</script>

<style >
</style>