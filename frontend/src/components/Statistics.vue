<template>
  <div id="app">
    <v-layout ma-5 justify-space-between>
      <v-card color="#444" width="500">
        <v-card-title class="justify-center">
          <v-subheader class="display-1 green--text">Transactions Income</v-subheader>
        </v-card-title>
        <apexchart
          type="line"
          :options="TransactionsIncomeExpenseExchangeNumberChart"
          :series="TransactionsIncomeChartData"
        />
      </v-card>

      <v-card color="#444" width="500">
        <v-card-title class="justify-center">
          <v-subheader class="display-1 green--text">Transactions Expense</v-subheader>
        </v-card-title>
        <apexchart
          type="line"
          :options="TransactionsIncomeExpenseExchangeNumberChart"
          :series="TransactionsExpenseChartData"
        />
      </v-card>
    </v-layout>

    <v-layout ma-5 justify-space-between>
      <v-card color="#444" width="500">
        <v-card-title class="justify-center">
          <v-subheader class="display-1 green--text">Exchange number</v-subheader>
        </v-card-title>
        <apexchart
          type="area"
          :options="TransactionsIncomeExpenseExchangeNumberChart"
          :series="ExchangenumberChartData"
        />
      </v-card>

      <v-card color="#444" width="500">
        <v-card-title class="justify-center">
          <v-subheader class="display-1 green--text">Valuta RON TO</v-subheader>
        </v-card-title>
        <apexchart type="bar" :options="ValutaRonChart" :series="ValutaRonChartData" />
      </v-card>
    </v-layout>
  </div>
</template>

<script>
import AuthRequest from "@/services/AuthService";

export default {
  name: "Statistic",
  data() {
    return {
      TransactionsIncomeExpenseExchangeNumberChart: {
        chart: {
          background: "#444",
          toolbar: {
            show: true,
            tools: {
              download: true,
              selection: false,
              zoom: false,
              zoomin: false,
              zoomout: false,
              pan: false,
              reset: false
            }
          }
        },
        colors: ["#4caf50"],
        xaxis: {
          labels: {
            style: {
              colors: "#4caf50"
            },
            formatter: function(timeStamp) {
              let date = new Date(timeStamp);
              var day = date.getDate();
              var month = date.getMonth() + 1;
              var year = date.getFullYear() % 100;
              date = year + "-" + month + "-" + day;
              return date;
            }
          }
        },
        yaxis: {
          labels: {
            style: {
              color: "#4caf50"
            }
          }
        }
      },
      TransactionsExpenseChartData: [
        {
          name: "Value",
          data: []
        }
      ],
      TransactionsIncomeChartData: [
        {
          name: "Value",
          data: []
        }
      ],
      ValutaRonChart: {
        chart: {
          background: "#444",
          toolbar: {
            show: true,
            tools: {
              download: true,
              selection: false,
              zoom: false,
              zoomin: false,
              zoomout: false,
              pan: false,
              reset: false
            }
          }
        },
        legend: {
          showForSingleSeries: false,
          showForNullSeries: true,
          showForZeroSeries: true,
          labels: {
            colors: "#ffffff"
          }
        },
        colors: ["#4caf50", "#2f6a31", "#173518"],
        xaxis: {
          categories: ["EUR", "USD", "GBP"],
          labels: {
            style: {
              colors: "#4caf50"
            }
          }
        },
        yaxis: {
          labels: {
            style: {
              color: "#4caf50"
            }
          }
        }
      },
      ValutaRonChartData: [
        {
          name: "https://www.otpbank.ro/hu/valutarfolyam",
          data: []
        },
        {
          name: "http://www.lillapanzio.ro/valutavalto",
          data: []
        },
        {
          name:
            "https://www.curs-valutar-bnr.ro/curs-valutar-banci/unicredit-tiriac-bank",
          data: []
        }
      ],
      ExchangenumberChartData: [
        {
          name: "Exchange Number",
          data: []
        }
      ]
    };
  },
  methods: {
    async StatisticExpenseIncome() {
      const responseIncome = await AuthRequest.statisticIncome(1);
      for (let index = 0; index < responseIncome.length; index++) {
        this.TransactionsIncomeChartData[0].data[index] = [
          responseIncome[index].date,
          responseIncome[index].amount
        ];
      }
      const responseExpense = await AuthRequest.statisticExpense(1);
      for (let index = 0; index < responseExpense.length; index++) {
        this.TransactionsExpenseChartData[0].data[index] = [
          responseExpense[index].date,
          responseExpense[index].amount
        ];
      }
    },
    async StatisticValutaRon() {
      const response = await AuthRequest.statisticValuta("valuta");
      this.ValutaRonChartData[0].name = response[0].web_address;
      this.ValutaRonChartData[0].data = [
        response[0].purchase_price,
        response[1].purchase_price,
        response[2].purchase_price
      ];
      this.ValutaRonChartData[1].name = response[3].web_address;
      this.ValutaRonChartData[1].data = [
        response[3].purchase_price,
        response[4].purchase_price,
        response[5].purchase_price
      ];
      this.ValutaRonChartData[2].name = response[6].web_address;
      this.ValutaRonChartData[2].data = [
        response[6].purchase_price,
        response[7].purchase_price,
        response[8].purchase_price
      ];
    },
    async StatisticExchanegNumber() {
      const responseExchangeNumber = await AuthRequest.statisticExchangeNumber(
        1
      );
      for (let index = 0; index < responseExchangeNumber.length; index++) {
        this.ExchangenumberChartData[0].data[index] = [
          responseExchangeNumber[index].date,
          responseExchangeNumber[index].number
        ];
      }
    }
  },
  mounted() {
    this.StatisticExpenseIncome();
    this.StatisticValutaRon();
    this.StatisticExchanegNumber();
  }
};
</script>

<style scoped>
</style>