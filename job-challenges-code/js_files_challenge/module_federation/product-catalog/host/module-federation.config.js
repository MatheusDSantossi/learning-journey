const mfConfig = {
  name: "host", // required
  remotes: {
    remote: "remote@http://localhost:8081/remoteEntry.js",
  }, // can be empty
  exposes: {}, // can be empty
  shared: {
    react: { singleton: true, eager: true, requiredVersion: "^19.0.0" },
    "react-dom": { singleton: true, eager: true, requiredVersion: "^19.0.0" },
  }, // can be empty or shared libs
  dts: false,
};

export default mfConfig;
