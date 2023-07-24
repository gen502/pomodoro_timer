const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    target: 'electron-renderer',
    resolve: {
      fallback: {
        "fs": false,
        "path": require.resolve("path-browserify")
      }
    }
  }
});
