<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-fab-transition>
        <v-btn
          @click="getTransactionTypes"
          v-on="on"
          color="green"
          fab
          dark
          small
          absolute
          left
          top
        >
          <v-icon>fas fa-plus</v-icon>
        </v-btn>
      </v-fab-transition>
    </template>

    <v-card elevation="10" dark outlined :loading="loadingCard">
      <v-toolbar extended flat>
        <v-toolbar-title class="ml-5">Add Transaction</v-toolbar-title>
        <template v-slot:extension>
          <v-tabs class="ml-2" v-model="tabs">
            <v-tab href="#income">Income</v-tab>
            <v-tab href="#expense">Expense</v-tab>
            <v-tabs-slider color="green" />
          </v-tabs>
        </template>
      </v-toolbar>
      <v-card-text>
        <v-tabs-items v-model="tabs">
          <v-tab-item
            v-for="content in ['income', 'expense']"
            v-model="value"
            :key="content"
            :value="content"
          ></v-tab-item>
        </v-tabs-items>
      </v-card-text>
      <v-layout mx-4 justify-space-around>
        <v-flex md5>
          <v-select
            :disabled="disableType"
            type="category"
            name="category"
            v-model="category"
            class="mr-5"
            item-text="name"
            :items="transactionTypes"
            label="Type"
            color="green"
            item-color="green"
            :rules="[ value =>!! value || 'Type is required!']"
          />
        </v-flex>

        <v-form ref="form" lazy-validation>
          <v-flex>
            <v-text-field
              label="Amount"
              color="green"
              clearable
              counter="9"
              hint="Up to 3 decimal places allowed"
              name="amount"
              :rules="[ value => /^\d+(\.\d{1,3})?$/.test(value) || 'Invalid input number!']"
              @keyup.enter="verification"
              v-model="amount"
            />
          </v-flex>
        </v-form>
      </v-layout>
      <v-flex mx-2>
        <v-text-field
          class="mx-5"
          label="Comment"
          color="green"
          clearable
          counter="50"
          name="comment"
          v-model="comment"
          @keyup.enter="verification"
        />
      </v-flex>

      <v-fab-transition>
        <v-btn
          class="ml-2"
          :key="activeSign.icon"
          :color="activeSign.color"
          fab
          large
          dark
          :ripple="false"
        >
          <v-icon>{{ activeSign.icon }}</v-icon>
        </v-btn>
      </v-fab-transition>
      <v-divider />

      <v-card-actions>
        <v-spacer />
        <v-btn @click="verification" color="success" text>Add</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
    <v-snackbar v-model="regSuccesSnackbar" class="mb-5 green--text">
      {{ regSuccesMsg }}
      <v-btn text @click="regSuccesSnackbar = false">Close</v-btn>
    </v-snackbar>
    <v-snackbar v-model="regFailedSnackbar" class="mb-5 red--text">
      {{ regFailedMsg }}
      <v-btn text @click="regFailedSnackbar = false">Close</v-btn>
    </v-snackbar>
  </v-dialog>
</template>

<script>
import AuthRequest from "@/services/AuthService";
export default {
  name: "CreateTransactionDialog",
  data() {
    return {
      dialog: false,
      loadingCard: false,
      transactionTypes: null,
      fab: false,
      hidden: false,
      tabs: null,
      disableType: false,
      category: "",
      amount: null,
      depositRON: 0,
      regFailedMsg: "",
      regSuccesMsg: "",
      regFailedSnackbar: false,
      regSuccesSnackbar: false,
      comment: "",
      value: "",
      userid: ""
    };
  },
  mounted() {
    this.userid = localStorage.getItem("userid");
  },
  methods: {
    async getDeposit() {
      const deposit = await AuthRequest.getdeposit(this.userid);
      this.depositRON = deposit.ron;
    },
    async verification() {
      if (this.$refs.form.validate()) {
        await this.getDeposit();
        if (this.tabs == "expense") {
          if (this.amount > this.depositRON) {
            this.regFailedMsg = "You have not enough money!";
            setTimeout(
              () => (this.regSuccesSnackbar = false),
              (this.regFailedSnackbar = true),
              1000
            );
            setTimeout(() => (this.regFailedSnackbar = false), 1000);
          } else {
            var new_deposit =
              parseFloat(this.depositRON) - parseFloat(this.amount);
            const response = await AuthRequest.changedeposit({
              id: this.userid,
              new_deposit: new_deposit,
              currency: "ron"
            });
            this.sendTransaction();
          }
        } else {
          var new_deposit =
            parseFloat(this.depositRON) + parseFloat(this.amount);
          console.log(new_deposit);
          const response = await AuthRequest.changedeposit({
            id: this.userid,
            new_deposit: new_deposit,
            currency: "ron"
          });
          this.sendTransaction();
        }
      }
    },

    async getTransactionTypes() {
      const transactionTypes = await AuthRequest.gettransactiontypes();
      this.transactionTypes = transactionTypes;
    },

    async sendTransaction() {
      const response = await AuthRequest.sendtransaction({
        id: this.userid,
        category: this.category,
        amount: this.amount,
        type: this.tabs,
        comment: this.comment
      });
      this.activateSnackbar(response);
    },

    activateSnackbar(response) {
      if (response.data.error) {
        this.regFailedMsg = response.data.error;
        setTimeout(() => (this.regSuccesSnackbar = false),(this.regFailedSnackbar = true),1000);
        this.loadingCard = "success";
        setTimeout(() => ((this.loadingCard = false), (this.regFailedSnackbar = false)),1000);
      } else {
        this.regSuccesMsg = response.data.message;
        setTimeout(() => (this.regFailedSnackbar = false),(this.regSuccesSnackbar = true),1000);
        this.$refs.form.reset();
        this.comment = "";
        this.loadingCard = "success";
        setTimeout(() => ((this.loadingCard = false),(this.regSuccesSnackbar = false),(this.dialog = false)),1000);
        this.$emit("refresh-event");
        setTimeout(() => location.reload(), 1000);
      }
    }
  },

  computed: {
    activeSign() {
      switch (this.tabs) {
        case "income": {
          this.disableType = true;
          return { color: "success", icon: "fas fa-plus" };
        }
        case "expense": {
          this.Type = "Type";
          this.disableType = false;
          return { color: "red", icon: "fas fa-minus" };
        }
        default:
          return {};
      }
    }
  }
};
</script>
<style />