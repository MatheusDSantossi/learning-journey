const mfConfig = {
  name: "host", // required
  filename: "remoteEntry.js", // required even if host has no remotes
  remotes: {}, // can be empty
  exposes: {}, // can be empty
  shared: {
    react: { singleton: true, eager: true, requiredVersion: "^18.0.0" },
    "react-dom": { singleton: true, eager: true, requiredVersion: "^18.0.0" },
  }, // can be empty or shared libs
};

export default mfConfig;
