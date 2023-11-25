<template>
  <div v-if="display" class="welcome-new">
    <v-dialog
      v-model="show"
      width="100%"
      persistent
      content-class="welcome-diag"
      hide-overlay
    >
      <v-card dark>
        <v-card-title>
          <!-- Welcome  -->
        </v-card-title>
        <v-card-text
          :class="`focus-${step < 3 ? 'true' : focused ? 'true' : 'false'}`"
        >
          <div style="min-height: 500px">
            <span id="text" class="welcome-text" :class="{ typing: step == 0 }">
              <span class="order">{{ ">>> " }}</span>
            </span>
            <br />
            <br />
            <span
              id="text2"
              class="welcome-text"
              :class="{ typing: step == 1, 'd-none': step == 0 }"
            >
              <span class="order">{{ ">>> " }}</span>
            </span>
            <br />
            <br />
            <span
              id="text3"
              class="welcome-text"
              :class="{ typing: step == 2, 'd-none': step < 2 }"
            >
              <span class="order">{{ ">>> " }}</span>
            </span>
            <br />
            <br />
            <span
              id="text4"
              class="welcome-text"
              :class="{ typing: step == 3, 'd-none': step < 3 }"
            >
              <span class="order">{{ ">>> " }} {{ value }}</span>
              <input
                ref="ghost"
                v-model="value"
                type="text"
                class="ghost-input d-nonecs"
                @keyup.enter="onEnter"
                @focus="focused = true"
                @blur="focused = false"
              />
            </span>
            <br />
            <br />
            <span
              id="text5"
              class="welcome-text"
              :class="{ typing: step == 4, 'd-none': step < 4 }"
            >
              <span class="order">{{ ">>> " }} {{ inputValue }}</span>
              <template
                v-if="
                  value.toLowerCase() === 'l' || value.toUpperCase() === 'L'
                "
              >
                <input
                  ref="ghost2"
                  v-model="inputValue"
                  type="text"
                  class="ghost-input d-nonecs"
                  @keyup.enter="onEnterValue"
                  @focus="focused = true"
                  @blur="focused = false"
                  autofocus
                />
              </template>
              <template v-else>
                <span id="text6" class="order progress-wrap" ref="text6">
                  [
                  <span
                    v-for="ind in i"
                    :key="`prog-${ind}`"
                    class="progress-bar"
                  ></span>
                </span>
              </template>
            </span>
            <br />
            <br />
            <span class="order welcome-text" v-if="step === 5 && response">
              {{ ">>> " }}
              <pre style="white-space: pre-wrap">{{ response }}</pre>
            </span>
            <br />
            <br />
            <span
              v-for="(payload, index) in payloads"
              :key="index"
              id="text10"
              class="welcome-text"
              :class="{ typing: step3 === 7, 'd-none': step3 < 7 }"
            >
              <br />
              <span
                ><span class="order"> {{ ">>> " }}</span> Would you like to
                download the output.txt file or want to continue (d/c/0)?</span
              >
              <br />
              <br />
              <pre class="order">{{ ">>> " }} {{ userInputs[index] }}</pre>
              <br />
              <pre class="order">{{ ">>> " }} {{ userValues[index] }}</pre>
              <br />
              <span class="order"
                >{{ ">>> " }}
                <pre style="white-space: pre-wrap"> {{ payload }}</pre>
              </span>
            </span>
            <br />
            <br />
            <span
              id="text7"
              class="welcome-text"
              :class="{
                typing: step === 7 && !showStep8,
                'd-none': step < 7 && !response,
              }"
            >
              <span class="order">{{ ">>> " }}</span>
            </span>

            <br />
            <br />

            <span id="text8" class="welcome-text" v-if="showStep8">
              <span class="order">{{ ">>> " }} {{ userInput }}</span>
              <input
                ref="ghost3"
                v-model="userInput"
                type="text"
                class="ghost-input d-nonecs"
                @keyup.enter.prevent="onEnterUserInput"
                @focus="focused = true"
                @blur="focused = false"
                autofocus
              />
            </span>
            <br />
            <br />
            <span
              id="text9"
              class="welcome-text"
              :class="{ typing: step3 === 9, 'd-none': step3 < 9 }"
            >
              <span class="order">{{ ">>> " }} {{ userValue }}</span>
              <input
                ref="ghost4"
                v-model="userValue"
                type="text"
                class="ghost-input d-nonecs"
                @keyup.enter="onEnterUserValue"
                @focus="focused = true"
                @blur="focused = false"
                autofocus
              />
            </span>
            <br />
            <br />
          </div>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "WelcomeComponent",
  props: {
    display: {
      type: Boolean,
      default() {
        return false;
      },
    },
    done: {
      type: Function,
      default() {
        return () => console.log("no function provided");
      },
    },
  },
  data() {
    return {
      show: true,
      focused: false,
      inputValue: "",
      userInput: "",
      value: "",
      userValue: "",
      response: "",
      userResponse: "",
      step: 0,
      step2: 0,
      step3: 0,
      payloads: [],
      userInputs: [],
      userValues: [],
      string: `Hello yash, Welcome to Cyber3ra. We are here to explore Cyber3ra's New App`,
      string2: `Let's get to the new era, Are you ready to begin?`,
      string3: `Press E to Begin; Or Press L to Linux; 0 to Exit;`,
      string4: `Would you like to download the output.txt file or want to continue (d/c/0)?`,
      i: 0,
      timings: [50, 400, 500, 50, 30, 50, 200, 400, 300, 400, 50],
      ins: false,
      showStep8: false,
      showStep9: false,
    };
  },
  watch: {
    ins(to, from) {
      console.log("new : ", to, "old : ", from);
      if (!to) {
        console.log("yeah new ", this.step2, to);
        if (this.step2 === 6) {
          console.log("setting/....");
          localStorage.setItem("new_user", "true");
          this.ins = false;
        } else {
          this.ins = true;
        }
      } else {
        this.ins = true;
      }
    },
  },
  mounted() {
    // console.log(this.display)
    if (this.display) {
      this.type();
    }
  },
  methods: {
    type() {
      if (this.i < this.string.length) {
        document.getElementById("text").innerHTML += this.string.charAt(this.i);
        this.i++;
        setTimeout(this.type, 50);
      } else {
        setTimeout(() => {
          this.i = 0;
          this.step += 1;
          this.type2();
        }, 1000);
      }
    },
    type2() {
      if (this.i < this.string2.length) {
        document.getElementById("text2").innerHTML += this.string2.charAt(
          this.i
        );
        this.i++;
        setTimeout(this.type2, 50);
      } else {
        setTimeout(() => {
          this.i = 0;
          this.step += 1;
          this.type3();
        }, 500);
      }
    },
    type3() {
      if (this.i < this.string3.length) {
        document.getElementById("text3").innerHTML += this.string3.charAt(
          this.i
        );
        this.i++;
        setTimeout(this.type3, 50);
      } else {
        setTimeout(() => {
          this.i = 0;
          this.step += 1;
          this.$nextTick(() => {
            this.$refs.ghost.focus();
          });
        }, 200);
      }
    },
    onEnter(e) {
      if (this.value === "e" || this.value === "E") {
        this.step += 1;
        this.type4();
        localStorage.setItem("new_user", "true");
      } else if (this.value === "l" || this.value === "L") {
        this.step += 1;
        this.$nextTick(() => {
          const ghost2 = this.$refs.ghost2;
          if (ghost2) {
            ghost2.focus();
          }
        });
      } else if (this.value === "0") {
        this.show = false;
      } else {
        this.$store.commit("showSnack", {
          message: "Please enter valid input",
          type: "error",
          timeout: 2000,
        });
      }
    },

    type4() {
      if (this.i < 20) {
        // document.getElementById("text4").innerHTML += this.string3.charAt(this.i);
        this.i++;
        setTimeout(
          this.type4,
          this.timings[Math.floor(Math.random() * this.timings.length)]
        );
      } else {
        // document.getElementById("text5").innerHTML += " ]";
        //   setTimeout(()=>{this.i = 0;this.step += 1;this.$nextTick(() => {
        //   this.$refs.ghost.focus()
        // })}, 200);
        this.$refs.text6.innerHTML += " ]";
        setTimeout(() => {
          this.show = false;
          this.ins = true;
          this.step2 += 1;
          this.i = 0;
        }, 700);
      }
    },

    onEnterValue(e) {
      if (e.keyCode === 13) {
        if (this.inputValue.trim() === "") {
          // If the input field is empty, show an alert message
          window.alert("Please enter a value in the input field.");
        } else {
          // If the input field is not empty, process the entered value
          this.sendValue();
        }
      }
    },
    sendValue: async function () {
      try {
        const response = await axios.post("http://127.0.0.1:8000/execute/", {
          command: this.inputValue,
        });
        console.log(response);
        this.response = response.data.output;
        // this.payloads.push(response.data.output);
        this.step++;
        this.type6();
      } catch (error) {
        console.log(error);
      }
    },
    type6() {
      if (this.i < this.string4.length) {
        document.getElementById("text7").innerHTML += this.string4.charAt(
          this.i
        );
        this.i++;
        setTimeout(this.type6, 60);
      } else {
        this.$nextTick(() => {
          this.showStep8 = true;

          this.$nextTick(() => {
            const ghost3 = this.$refs.ghost3;
            if (ghost3) {
              ghost3.focus();
            }
          });
        });
      }
    },

    onEnterUserInput: async function (e) {
      e.preventDefault();
      if (this.userInput === "d" || this.userInput === "D") {
        try {
          const response = await axios.get("http://127.0.0.1:8000/download/", {
            responseType: "blob",
          });
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "filename.txt");
          document.body.appendChild(link);
          link.click();
        } catch (error) {
          console.log(error);
        }
      } else if (this.userInput.toLowerCase() === "c") {
        this.step3 = 9;
        this.showStep9 = true;
        this.userResponse = "";
        this.userValue = "";
        this.userInputs.push("c");
        if (this.step3 === 9) {
          this.$nextTick(() => {
            const ghost4 = this.$refs.ghost4;
            if (ghost4) {
              ghost4.focus();
            }
          });
        }
      } else if (this.userInput === "0") {
        this.show = false;
      } else {
        this.$store.commit("showSnack", {
          message: "Please enter valid input",
          type: "error",
          timeout: 2000,
        });
      }
    },
    onEnterUserValue(e) {
      if (e.keyCode === 13) {
        if (this.userValue.trim() === "") {
          // If the input field is empty, show an alert message
          window.alert("Please enter a value in the input field.");
        } else {
          // If the input field is not empty, process the entered value
          this.sendUserValue();
        }
      }
    },
    sendUserValue: async function () {
      try {
        const response = await axios.post("http://127.0.0.1:8000/execute/", {
          command: this.userValue,
        });
        console.log(response);
        // this.userResponse = response.data.output;
        this.userValues.push(this.userValue);
        this.payloads.push(response.data.output);
        this.step3 = 8;
        this.userInput = "";
        this.type6();
        this.userValue = "";

        this.$nextTick(() => {
          const ghost4 = this.$refs.ghost4;
          if (ghost4) {
            ghost4.focus();
          }
        });

        // const dialogContainer = this.$el;
        // if (dialogContainer) {
        //   dialogContainer.scrollTop = dialogContainer.scrollHeight;
        // }

        // if (this.userResponse) {
        //   this.showStep9 = false;
        // }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
<style scoped>
body {
  overflow: hidden !important;
}

.profile-icon {
  position: absolute;
  padding: 3px;
  background-color: white;
  border-radius: 50rem;
  z-index: 5200;
  right: 17px;
  top: 14px;
}

.progress-bar {
  width: 30px;
  margin-left: 5px;
  margin-right: 5px;
  background-color: #149414;
  height: 50px;
  padding: 0px 8px;
}

@media (max-width: 576px) {
  .progress-bar {
    width: 10px;
    margin-left: 4px;
    margin-right: 4px;
    padding: 0px 4px;
  }
}

.ghost-input::-moz-selection {
  /* Code for Firefox */
  color: #0f1725;
  background: #0f1724;
}

.ghost-input::selection {
  color: #0f1725;
  background: #0f1724;
}

.ghost-input {
  caret-color: transparent;
  -webkit-touch-callout: none;
  /* iOS Safari */
  -webkit-user-select: none;
  /* Safari */
  -khtml-user-select: none;
  /* Konqueror HTML */
  -moz-user-select: none;
  /* Old versions of Firefox */
  -ms-user-select: none;
  /* Internet Explorer/Edge */
  user-select: none;
  color: #149414;
  color: transparent;
  outline: 0;
  border: none;
  background: transparent;
  width: 100%;
  position: absolute;
  left: 0;
  height: 100%;
  top: 0;
}

.default .v-overlay--active .v-overlay__scrim,
.welcome-diag .v-overlay--active .v-overlay__scrim {
  opacity: 0.95 !important;
  background-color: rgb(10, 10, 10) !important;
}

.default .v-overlay--active {
  z-index: 7 !important;
}

.welcome-text {
  font-family: monospace !important;
  font-size: 25px;
  user-select: none;
}

.focus-true .typing {
  border-right: 5px solid #149414;
  padding-right: 5px;
  animation: type 500ms infinite;
}

.order {
  color: #149414;
  text-shadow: 2px 2px 5px #149414;
  font-family: monospace !important;
  margin-right: 5px;
}

@keyframes type {
  0% {
    border-right: 5px solid #149414;
  }

  50% {
    border-right: 5px solid transparent;
  }

  100% {
    border-right: 5px solid #149414;
  }
}
</style>
