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
            <v-img :src="user.picture"></v-img>
          </v-avatar>
        </v-list-item>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="far fa-user"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Username</v-list-item>
        <v-list-item class="subtitle-1" v-text="user.name"></v-list-item>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
          <v-icon class="far fa-clock"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Birth date</v-list-item>

        <v-list-item class="subtitle-1" v-text="user.birth_date"></v-list-item>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
        	<v-icon class="fas fa-venus-mars"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Gender</v-list-item>
        <v-list-item class="subtitle-1" v-text="user.gender"></v-list-item>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
        	<v-icon class="fas fa-unlock-alt"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Password</v-list-item>
        <v-list-item class="subtitle-1" v-text="user.password"></v-list-item>
        <v-btn outlined color="success" text>Change</v-btn>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
            <v-icon class="fas fa-calendar-check"></v-icon>
        </v-list-item-icon>
        <v-list-item class="overline">Data_accession</v-list-item>
        <v-list-item class="subtitle-1" v-text="user.data_accession"></v-list-item>
      </v-list-item>
    </v-card>

    <v-card dark class="mt-5">
      <v-card-title primary-title class="justify-center">
        <v-subheader class="display-1 white--text">Connection Data</v-subheader>
      </v-card-title>
      <v-list>
        <v-list-item>
			<v-list-item-icon>
				<v-icon class="far fa-envelope"></v-icon>
			</v-list-item-icon>
			<v-list-item class="overline">Email Address</v-list-item>
			<v-list-item class="subtitle-1" v-text="user.email_address"></v-list-item>
        </v-list-item>

        <v-list-item>
			<v-list-item-icon>
				<v-icon class="fas fa-mobile-alt"></v-icon>
			</v-list-item-icon>
			<v-list-item class="overline">Telephone Number</v-list-item>
			<v-list-item class="subtitle-1" v-text="user.telephone_number"></v-list-item>
        </v-list-item>

        <v-list-item>
            <v-list-item-icon>
              <v-icon class="fas fa-comments-dollar"></v-icon>
            </v-list-item-icon>
            <v-list-item class="overline">Deposit</v-list-item>
            <v-list-item class="subtitle-1 ml-5 pl-5">{{user.deposit}} RON</v-list-item>
              <exchange-card-dialog :currency="'RON'" />
        </v-list-item>

      </v-list>
    </v-card>
  </div>
</template>

<script>
import ExchangeCardDialog from "./fittings/ExchangeCardDialog";

export default {
  name: "Account",
  components: { ExchangeCardDialog },
  data() {
    isMobile: false;
    return {
      user: {
        picture: "https://randomuser.me/api/portraits/women/72.jpg",
        name: "Nagy Tünde",
        birth_date: "1997-09-05",
        gender: "Female",
        password: "alfabetaalfa",
        data_accession: "2019-11-06",
        email_address: "nagyserbantunde@gmail.com",
        telephone_number: "0729461392",
        deposit: "1467,4"
      }
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

  methods: {
    onResize() {
      this.isMobile = window.innerWidth < 600;
    }
  }
};
</script>

<style >
</style>