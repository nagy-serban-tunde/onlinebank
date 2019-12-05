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

    <v-card elevation="10" dark outlined>
      <v-toolbar extended flat>
        <v-toolbar-title class="ml-5">Add Exchange</v-toolbar-title>
        <template v-slot:extension>
          <v-tabs class="ml-2" v-model="tabs">
            <v-tab href="#one">Income</v-tab>
            <v-tab href="#two">Expense</v-tab>
            <v-tabs-slider color="green" />
          </v-tabs>
        </template>
      </v-toolbar>
      <v-card-text>
        <v-tabs-items v-model="tabs">
          <v-tab-item v-for="content in ['one', 'two']" :key="content" :value="content"></v-tab-item>
        </v-tabs-items>
      </v-card-text>
      <v-layout mx-4 justify-space-around>
        <v-flex md5>
          <v-select
            :disabled="disableType"
            type="type"
            name="type"
            v-model="type"
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
              counter="10"
              hint="Up to 3 decimal places allowed"
              name="amount"
              :rules="[ value => /^\d+(\.\d{1,3})?$/.test(value) || 'Invalid input number!']"
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
      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer />
        <v-btn @click="adding" color="success" text>Add</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import AuthRequest from "@/services/AuthService";
export default {
  name: "CreateTransactionDialog",
  data() {
    return {
      dialog: false,
      transactionTypes: null,
      fab: false,
      hidden: false,
      tabs: null,
      disableType: false,
    };
  },
  methods: {
    async getTransactionTypes() {
      const transactionTypes = await AuthRequest.gettransactiontypes();
      this.transactionTypes = transactionTypes;
    }
  },
  computed: {
    activeSign() {
      switch (this.tabs) {
        case "one": {
          this.disableType = false;
          return { color: "success", icon: "fas fa-plus" };
        }
        case "two": {
          this.Type = "Type";
          this.disableType = true;
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