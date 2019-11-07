<template>
    <div>
			<v-card dark >
				<v-card-title primary-title class="justify-center">
					<v-subheader class="display-1 white--text">Personal data</v-subheader>
				</v-card-title>
				<v-list-item>
					<v-list-item-content >

						<v-col>
						<v-container>
							<v-row>
								<v-col>
									<v-subheader class="title">Name:</v-subheader>
									<v-list-item class="title">{{user.name}} </v-list-item>
								</v-col>
							</v-row>

							<v-row>
								<v-col>
									<v-subheader class="title">Birth date:</v-subheader>
									<v-list-item class="title">{{user.birthdate}} </v-list-item>
								</v-col>
							</v-row>

							<v-row>
								<v-col>
									<v-subheader class="title">E-mail:</v-subheader>
									<v-list-item class="title">{{user.email}} </v-list-item>
								</v-col>
							</v-row>

							<v-row>
								<v-col>
									<v-subheader class="title">Deposit:</v-subheader>
									<v-list-item class="title">{{user.deposit}} </v-list-item>
									<v-layout >
										<v-card-actions color="green">
											<v-btn outlined color="success" text>Add</v-btn>
										</v-card-actions>
									</v-layout>
								</v-col>
							</v-row>

							<v-row>
								<v-col>
									<v-subheader class="title">Data accession:</v-subheader>
									<v-list-item class="title">{{user.data_accession}} </v-list-item>
								</v-col>
							</v-row>

						</v-container>
						</v-col>

						<v-col>
						<v-container>
							<v-row>
								<v-col>
									<v-avatar size="300">
              							<v-img src="https://randomuser.me/api/portraits/women/72.jpg"></v-img>
           							</v-avatar>
								</v-col>
							</v-row>
						</v-container>
						</v-col>

					</v-list-item-content>
				</v-list-item>
			</v-card>
    </div>
</template>

<script>

export default {
	name : "Account",
	data(){
		return{
			user: {
        name: "Nagy Tünde",
        email: "nagyserbantunde@gmail.com",
        birthdate: "1997-09-05",
				deposit: "1467.4",
				data_accession: "2019-11-06",
        picture: "https://randomuser.me/api/portraits/women/72.jpg"
      }
		}
	}		
}
</script>

<style scoped>
</style>