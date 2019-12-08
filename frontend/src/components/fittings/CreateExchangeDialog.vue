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
      <v-card-title>Add Exchange</v-card-title>
      <v-layout justify-space-around>
        <v-flex md4>
          <v-select
            :disabled="disableType"
            type="currencyfrom"
            name="currencyfrom"
            v-model="currencyFrom"
            class="mr-5"
            item-text="name"
            :items="currencyList"
            label="Currency from"
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
              v-model="amount"
            />
          </v-flex>
        </v-form>
      </v-layout>
      <v-layout justify-space-around>
        <v-flex md4>
          <v-select
            :disabled="disableType"
            type="currencyto"
            name="currencyto"
            v-model="currencyTo"
            class="mr-5"
            item-text="name"
            :items="currencyList"
            label="Currency to"
            color="green"
            item-color="green"
            :rules="[ value =>!! value || 'Type is required!']"
          />
        </v-flex>

        <v-form ref="form" lazy-validation>
          <v-flex>
            <v-text-field
              class="mb-5"
              label="Result amount"
              color="green"
              clearable
              hint="Up to 3 decimal places allowed"
              name="resultAmount"
              disabled
              :rules="[ value => /^\d+(\.\d{1,3})?$/.test(value) || 'Invalid input number!']"
              v-model="resultAmount"
            />
          </v-flex>
        </v-form>
      </v-layout>
      <v-divider />

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
  name: "CreateExchangeDialog",
  data() {
    return {
      dialog: false,
      currencyList: ["RON", "EURO", "GBP", "USD"],
      currencyFrom: "",
      currencyTo: "",
      resultAmount: 0
    };
  },
  methods: {},
  computed: {
    compareCurrencies() {
      if (this.currencyFrom == this.currencyTo) {
        return false;
      }
      return true;
    }
  }
};
</script>
<style />