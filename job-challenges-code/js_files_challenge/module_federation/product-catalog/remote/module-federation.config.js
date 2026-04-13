const mfConfig = {
  name: "remote", // required
  remotes: {}, // can be empty
  exposes: { "./Reviews": "./src/Reviews.tsx" }, // can be empty
  shared: {
    react: { singleton: true, eager: true, requiredVersion: "^19.0.0" },
    "react-dom": { singleton: true, eager: true, requiredVersion: "^19.0.0" },
  }, // can be empty or shared libs
  dts: false,
};

export default mfConfig;
