# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import streamlit.components.v1 as components

LOGGER = get_logger(__name__)


def f(x: float) -> float:
    if x == 0:
        return 1
    else:
        return np.sin(x) / x


def g(x: float) -> float:
    return x*np.cos(x)


def h(x: float) -> float:
    if x == 0:
        return 0
    else:
        return 1/x



def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.title("Vending machine prediction model")
    st.write("Enter begin and end point")
    x1 = st.text_input("Begin")
    x2 = st.text_input("End")

    options = ['f(x)', 'g(x)', 'h(x)']
    option = st.selectbox("Choose the function: ", options)

    if x1 != "" and x2 != "":
      x1 = int(x1)
      x2 = int(x2)

      X = np.linspace(min(x1, x2), max(x1, x2), 1000)
      if option == 'f(x)':
        y = [f(x) for x in X]
      elif option == 'g(x)':
          y = [g(x) for x in X]
      elif option == 'h(x)':
          y = [h(x) for x in X]
      else:
          st.write("Damn")
      
      figure = plt.figure()
      plt.plot(X, y)
      X_2 = np.linspace(min(x1, x2), max(x1, x2), 1000)
      y = [0] * 1000
      plt.plot(X_2, y)
      fig_html = mpld3.fig_to_html(figure)
      components.html(fig_html, height=600)


if __name__ == "__main__":
    run()
