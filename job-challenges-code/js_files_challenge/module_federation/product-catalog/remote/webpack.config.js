const { ModuleFederationPlugin } = require("webpack").container;

module.exports = {
  // other wepack config
  plugins: [
    new ModuleFederationPlugin({
      name: "remote", // unique name
      filename: "remoteEntry.js", // output manifest file
      exposes: {
        "./Reviews": "./src/Reviews", // expose the Reviews component
      },
      shared: {
        react: { singleton: true, requiredVersion: "^18.2.0" },
        "react-dom": { singleton: true, requiredVersion: "^18.2.0" },
      },
    }),
  ],
};
