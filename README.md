# pomodoro_timer
Vue CLI Plugin Electron Builderを使うのが良さそうだったのでこれにしました.ファイル構成はまだ全部は把握しきれてないです(-_-;)

バージョンは以下の通りです

node.js
v16.13.0

npm
8.1.0

## Project setup
すでにインストールしている場合は必要ないです(vue -Vとかで何か出れば多分大丈夫)
```
npm install -g @vue/cli
```

### Compiles and hot-reloads for development
```
vue add electron-builder //毎回やる必要はないかも
npm run electron:serve
```
App.vueとかを変更して保存するとすぐに反映されます

各自ブランチを切って適当に編集して動かしてもらうと良いと思います.


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
