import { spawn } from "node:child_process";

const child = spawn("rspack", ["dev", "-c", "./rspack.config.mjs"], {
  shell: true,
  stdio: "inherit",
  env: {
    ...process.env,
    NODE_ENV: "development",
  },
});

child.on("exit", (code) => {
  process.exit(code ?? 0);
});
