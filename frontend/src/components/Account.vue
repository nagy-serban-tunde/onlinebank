<template>
  <div>
    <v-card dark>
      	<v-card-title primary-title class="justify-center">
        	<v-subheader class="display-1 white--text">Personal Data</v-subheader>
      	</v-card-title>

    	<v-list-item>
			<v-list-item-icon>
              <v-icon class="far fa-user"></v-icon>
            </v-list-item-icon>
			<v-list-item-title class="overline">Username</v-list-item-title>
            <v-list-item-title class="subtitle-1" v-text="user.name"> </v-list-item-title>
			
    	</v-list-item>

		<v-list-item>

			<v-list-item-title class="overline">Birth date</v-list-item-title>
            <v-list-item-title class="subtitle-1" v-text="user.birth_date"> </v-list-item-title>
			
    	</v-list-item>

		<v-list-item>

			<v-list-item-title class="overline">Gender</v-list-item-title>
            <v-list-item-title class="subtitle-1" v-text="user.gender"> </v-list-item-title>
			
    	</v-list-item>

		<v-list-item>

			<v-list-item-title class="overline">Password</v-list-item-title>
            <v-list-item-title class="subtitle-1" v-text="user.password"> </v-list-item-title>
			
    	</v-list-item>

		<v-list-item>

			<v-list-item-title class="overline">Data_accession</v-list-item-title>
            <v-list-item-title class="subtitle-1" v-text="user.data_accession"> </v-list-item-title>
			
    	</v-list-item>

    </v-card>

    <v-card dark class="mt-5">
      <v-card-title primary-title class="justify-center">
        <v-subheader class="display-1 white--text">Connection Data</v-subheader>
      </v-card-title>

      <v-list disabled>
        <v-list-item-group>
          <v-list-item v-for="(item, i) in items1" :key="i">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title class="overline" v-text="item.text"></v-list-item-title>
            </v-list-item-content>

            <v-list-item-content>
              <v-list-item-subtitle class="subtitle-1 white--text" v-text="item.data"></v-list-item-subtitle>
            </v-list-item-content>

            <!-- <v-divider></v-divider> -->
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>

    <!-- <v-card dark >
			<v-card-title primary-title class="justify-center">
				<v-subheader class="display-1 white--text">Personal Data</v-subheader>
			</v-card-title>

			<v-list-item>
				<v-list-item-content >
					<v-col>
						<v-row>
							<v-col>
								<v-row>
									<v-subheader class="title">Last Name: {{user.lastname}}</v-subheader>
								</v-row>

								<v-row>
									<v-subheader class="title">First Name: {{user.firstname}}</v-subheader>
								</v-row>

								<v-row>
									<v-subheader class="title">Birth date: {{user.birthdate}}</v-subheader>
								</v-row>
										
								<v-row>
									<v-subheader class="title"> Password: {{user.password}} </v-subheader>
								</v-row>
							</v-col>

							<v-col >
									<v-avatar size="200">
										<v-img class="justify-center" :src="user.picture"></v-img>
									</v-avatar>
							</v-col>
						</v-row>
						
						<v-divider ></v-divider>

						<v-list-item></v-list-item>
						<v-row>
							<v-col>
								<v-row>
									<v-subheader class="title">Email Address: {{user.email}} </v-subheader>
								</v-row>

								<v-row>
									<v-subheader class="title">Data accession: {{user.data_accession}}</v-subheader>
								</v-row>
							</v-col>

							<v-col>
								<v-subheader class="title justify-center">Deposit: {{user.deposit}} RON</v-subheader>
								<v-card-actions class="justify-center" color="green">
									<exchange-card-dialog :currency="'RON'"/>
								</v-card-actions>
							</v-col>

						</v-row>
					</v-col>
				</v-list-item-content>
			</v-list-item>
    </v-card>-->
  </div>
</template>

<script>
import Root from "./Root.vue";
import ExchangeCardDialog from "./fittings/ExchangeCardDialog";

export default {
  name: "Account",
  components: { Root, ExchangeCardDialog },
  data() {
    isMobile: false;
    return {
	  show: false,
	  user: {
		name: "Nagy Tunde",
		birth_date: "1997-09-05",
		gender: 'female',
		password: 'alfabetaalfa',
		data_accession: "2019-11-06",
		email: "nagyserbantunde@gmail.com",
		telephone_number: "0729461392",
        deposit: "1467.4"
      },
      items: [
        {
          text: "picture",
          icon: "fa-portrait",
          data: "https://randomuser.me/api/portraits/women/72.jpg"
        },
        { text: "name", icon: "fa-user", data: "Nagy Tünde" },
        { text: "birth date", icon: "mdi-clock", data: "1997-09-05" },
        { text: "gender", icon: "fa-venus-mars", data: "Female" },
        { text: "password", icon: "fa-unlock", data: "alfabetaalfa" },
        {
          text: "data accession",
          icon: "fa-calendar-check",
          data: "2019-11-06"
        }
      ],
      items1: [
        {
          text: "Email Address",
          icon: "fa-envelope-square",
          data: "nagyserbantunde@gmail.com"
        },
        {
          text: "telephone number",
          icon: "fa-phone-square-alt",
          data: "0729461392"
        },
        { text: "Deposit", icon: "fa-comments-dollar", data: "1467.4" }
      ]
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