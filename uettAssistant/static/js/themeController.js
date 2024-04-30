//This is the code for controlling theme of my website

const darkmodeicon = document.querySelector(".darkmodeicon");
const root = document.documentElement;
const themeColorMeta = document.querySelector('meta[name="theme-color"]');
const path = document.getElementById("darkModeIconPath");

let darkModeEnabled = localStorage.getItem("darkModePreference") === "true";

const prefersDarkMode = window.matchMedia(
  "(prefers-color-scheme: dark)"
).matches;

if (darkModeEnabled === null) {
  darkModeEnabled = prefersDarkMode;
} else {
  if (darkModeEnabled !== prefersDarkMode) {
    updateStyles();
  } else {
    updateStyles();
  }
}

darkmodeicon.addEventListener("click", () => {
  darkModeEnabled = !darkModeEnabled;
  updateStyles();
  localStorage.setItem("darkModePreference", darkModeEnabled);
});

function updateStyles() {
  if (darkModeEnabled) {
    themeColorMeta.setAttribute("content", "#151515");
    path.setAttribute(
      "d",
      "M479.933-294.001q-77.99 0-131.961-53.971-53.971-53.971-53.971-131.961 0-77.989 53.971-132.528 53.971-54.538 131.961-54.538 77.989 0 132.528 54.538 54.538 54.539 54.538 132.528 0 77.99-54.538 131.961-54.539 53.971-132.528 53.971ZM72.693-451.308q-11.67 0-20.18-8.563Q44-468.433 44-480.178t8.511-20.629q8.511-8.885 20.18-8.885h104.616q12.094 0 20.893 8.855Q207-491.982 207-479.804q0 11.752-8.799 20.124-8.799 8.372-20.893 8.372H72.693Zm709.999 0q-11.669 0-20.181-8.563Q754-468.433 754-480.178t8.511-20.629q8.512-8.885 20.181-8.885h104.615q12.094 0 20.893 8.855 8.799 8.855 8.799 21.033 0 11.752-8.799 20.124-8.799 8.372-20.893 8.372H782.692ZM479.804-754q-11.752 0-20.124-8.511-8.372-8.512-8.372-20.181v-104.615q0-12.094 8.563-20.893 8.562-8.799 20.307-8.799t20.629 8.799q8.885 8.799 8.885 20.893v104.615q0 11.669-8.855 20.181Q491.982-754 479.804-754Zm0 710q-11.752 0-20.124-8.512-8.372-8.511-8.372-20.18v-104.616q0-12.094 8.563-20.893Q468.433-207 480.178-207t20.629 8.799q8.885 8.799 8.885 20.893v104.615q0 11.67-8.855 20.18Q491.982-44 479.804-44ZM246.385-674.386l-60.461-59.077q-8.693-8.692-8.982-20.651-.29-11.96 8.995-21.067 7.99-7.973 19.757-7.973 11.767 0 21.844 8.077L287-714.999q8.461 9.51 8.461 21.216 0 11.706-8.269 19.316-7.769 9.544-20.249 9.544-12.481 0-20.558-9.462Zm487.077 488.461L674-246.001q-9.461-8.128-8.961-19.458.5-11.33 9.461-21.541 7-8.077 18.819-8.009 11.819.067 21.296 8.394l60.461 59.077q7.693 9.692 7.982 21.651.29 11.96-7.995 20.067-9.425 8.973-20.975 8.973-11.549 0-20.626-9.077ZM674-673.808q-9.077-8.134-8.884-19.932.192-11.798 9.269-20.875l59.077-60.461q8.692-7.693 20.651-7.982 11.96-.29 21.067 7.995 7.973 9.425 7.973 20.975 0 11.549-8.077 20.626L714.999-674q-9.461 9.461-21.073 9.461-11.611 0-19.926-9.269ZM185.82-185.737q-8.973-8.19-8.973-19.957 0-11.767 9.077-21.844L246.001-287q8.03-8.077 19.476-8.077T286.385-287q8.307 8.5 8.115 20.519-.193 12.019-7.885 20.096l-59.077 60.461q-10.077 9.077-21.844 9.367-11.767.289-19.874-9.18Z"
    );

    root.style.setProperty("--bgcolor", "#151515");
    root.style.setProperty("--primaryColor", "transparent");
    root.style.setProperty("--primaryFooter", "#252525");
    root.style.setProperty("--headerElementColor", "#fffff0");
    root.style.setProperty("--h3color", "#ccc");
    root.style.setProperty("--h1color", "#ddd");
    root.style.setProperty("--coursecode", "#999");
    root.style.setProperty("--creditcolor", "#00000000");
    root.style.setProperty("--placeholder", "#444");
    root.style.setProperty("--inputColor", "#999");
    root.style.setProperty("--topborder", "#e8787e");
    root.style.setProperty("--cgpacalc", "#252525");
    root.style.setProperty("--togglebg", "#666");
    root.style.setProperty("--upfeature", "#252525");
    root.style.setProperty("--upfeatureh3", "#fffff0");
    root.style.setProperty("--upfeatureshadow", "transparent");
    root.style.setProperty("--homeButtonBg", "#252525");
    root.style.setProperty("--homeButtonBorder", "transparent");
    document.getElementById("allHeader").style.backdropFilter = "blur(10px)";
  } else {
    path.setAttribute(
      "d",
      "M240-383.922q42.615 0 77.999 23.615 35.385 23.616 53.461 63.231l13.616 33.154H422q33.307 0 57.614 24.808 24.308 24.807 24.308 59.114 0 35.307-24.615 59.114Q454.692-97.078 420-97.078H240q-59.692 0-101.307-41.615T97.078-240q0-59.692 41.615-101.807T240-383.922ZM433.306-820.69q-10.076 96.692 19.347 188.153 29.423 91.461 99.115 160.153 68.692 69.693 160.154 98.923 91.461 29.231 188.768 19.155-30 134.076-136.269 217.998-106.268 83.922-243.652 82.306-10.23 0-19.653-.5-9.423-.5-19.039-1.5 36.692-15.692 59.461-49.114 22.769-33.423 22.769-74.884 0-58.538-40.231-100.038t-97.154-43.653q-25.307-54.616-75.576-87.616-50.269-33-111.346-33-28.23 0-55.038 8.385-26.807 8.384-49.961 24.538-1-8.154-1-15.116v-15.115q-1-137.384 82.423-242.729Q299.846-789.69 433.306-820.69Z"
    );
    document.getElementById("allHeader").style.backdropFilter = "";
    themeColorMeta.setAttribute("content", "#c9222a");
    root.style.setProperty("--bgcolor", "#fffff0");
    root.style.setProperty("--primaryColor", "#c9222a");
    root.style.setProperty("--primaryFooter", "#041c32");
    root.style.setProperty("--headerElementColor", "#fffff0");
    root.style.setProperty("--h3color", "#555");
    root.style.setProperty("--h1color", "#000");
    root.style.setProperty("--coursecode", "#c9222a");
    root.style.setProperty("--creditcolor", "#041c32");
    root.style.setProperty("--placeholder", "#c9222a71");
    root.style.setProperty("--inputColor", "#ccc");
    root.style.setProperty("--topborder", "#c9222a");
    root.style.setProperty("--cgpacalc", "#fffff0");
    root.style.setProperty("--togglebg", "#ccc");
    root.style.setProperty("--upfeature", "#7fffd4");
    root.style.setProperty("--upfeatureshadow", "#04422e74");
    root.style.setProperty("--upfeatureh3", "#04422e");
    root.style.setProperty("--homeButtonBg", "#fffff0");
    root.style.setProperty("--homeButtonBorder", "#c9222a");
  }
}

updateStyles();
