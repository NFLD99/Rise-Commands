// ==UserScript==
// @name         Get Your Token [alt + T] | Login with token [alt + L]
// @namespace    https://nfld99.com/therabbithacks.io.html
// @version      0.1
// @description  Copy Or Download Your token
// @author       Mr.Fluff
// @match        https://discord.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=discord.com
// @grant        none
// @require     https://raw.githubusercontent.com/eligrey/FileSaver.js/master/dist/FileSaver.min.js
// ==/UserScript==

// If User Wants To Download The Token, Download A .Txt With The Account Name And Token Within
function dl(txt, name) {
    var blob = new Blob([txt], {type: "text/plain;charset=utf-8"});
    saveAs(blob, name + ".txt");
}

// Ask To Download Or Copy Token After Obtaining Token
function onAltt() {
    var tkn = (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    var cpy = confirm("Copy or Download Token? [ok = copy, Cancel = Download]")
    var dcn = document.querySelector("#app-mount > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div.container-1eFtFS > div > div.content-1SgpWY > div.sidebar-1tnWFu.hasNotice-1s68so > section > div.container-YkUktl > div.nameTag-sc-gpq.canCopy-IgTwyV > div.colorStandard-21JIj7.size14-3fJ-ot.usernameContainer-3PPkWq > div").innerText

// if "Ok" Copy Token To Clipboard
    if (cpy == true){
        navigator.clipboard.writeText(tkn)
    }

// If "Cancel" Download Token
    if (cpy !== true){
        dl(tkn, dcn)
    }
}
// Login With Token
function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }

// Ask For Token
function onAltl() {
    login(prompt("please Enter Your Token:"))
}

// Run Function To Get Token On Alt + T
function onKeydown(evt) {
    if (evt.altKey && evt.keyCode == 84) {
        onAltt();
    }
    if (evt.altKey && evt.keyCode == 76) {
        onAltl();
    }
}
document.addEventListener('keydown', onKeydown, true);
