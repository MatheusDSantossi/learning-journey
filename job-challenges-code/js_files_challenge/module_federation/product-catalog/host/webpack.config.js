const { ModuleFederationPlugin } = require("webpack").container;

module.exports = {
  // other wepack config
  plugins: [
    new ModuleFederationPlugin({
      name: "host", // unique name
      remotes: {
        remote: "remote@http://localhost:8081/remoteEntry.js", // reference remote
      },
      shared: {
        react: { singleton: true, requiredVersion: "^18.2.0" },
        "react-dom": { singleton: true, requiredVersion: "^18.2.0" },
      },
    }),
  ],
};
