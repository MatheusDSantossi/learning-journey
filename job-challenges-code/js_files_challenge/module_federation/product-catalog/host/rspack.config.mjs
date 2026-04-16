import path from "node:path";
import { fileURLToPath } from "node:url";
import { rspack } from "@rspack/core";
import ReactRefreshRspackPlugin from "@rspack/plugin-react-refresh";
import mfConfig from "./module-federation.config.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const isDev = process.env.NODE_ENV === "development";
const targets = ["chrome >= 87", "edge >= 88", "firefox >= 78", "safari >= 14"];

export default {
  context: __dirname,
  target: "web", // <-- required to fix the `.web` error
  client: {
    overlay: false,
  },
  entry: {
    main: "./src/index.tsx",
  },
  resolve: {
    extensions: ["...", ".ts", ".tsx", ".js", ".jsx"],
  },
  devServer: {
    port: 8080,
    historyApiFallback: true,
    //* This is a more robust solution to remove the error, however, disabling the HMR makes the dev slower. So, considering that on prod that won't be necessary we can go with a more simple option which is "client: {overlay: false}"
    // hot: false,
    // liveReload: false,
  },
  output: {
    uniqueName: "host",
    publicPath: "http://localhost:8080/",
  },
  experiments: { css: true },
  module: {
    rules: [
      {
        test: /\.(jsx?|tsx?)$/,
        use: [
          {
            loader: "builtin:swc-loader",
            options: {
              jsc: {
                parser: { syntax: "typescript", tsx: true },
                transform: {
                  react: {
                    runtime: "automatic",
                    development: isDev,
                    refresh: isDev,
                  },
                },
              },
              env: {
                targets,
              },
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new rspack.HtmlRspackPlugin({ template: "./index.html" }),
    new rspack.container.ModuleFederationPlugin({
      ...mfConfig,
      remotes: {
        remote: "remote@http://localhost:8081/remoteEntry.js",
        cart: "cart@http://localhost:8082/remoteEntry.js",
      },
      shared: {
        react: { singleton: true, eager: true, requiredVersion: "^19.0.0" },
        "react-dom": {
          singleton: true,
          eager: true,
          requiredVersion: "^19.0.0",
        },
      },
      dts: false,
    }),
    isDev ? new ReactRefreshRspackPlugin() : null,
  ].filter(Boolean),
};
