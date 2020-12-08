/*
 * feed.js v1.0.0-sha.1565aebfd7a95bf4fbf807524d7786c151c9d40f
 * (c) 2018 Playbuzz (http://www.playbuzz.com)
 */
!function(){function a(){window.PlayBuzz=window.PlayBuzz||{},PlayBuzz.asyncListeners=[],PlayBuzz.on=function(a,b){PlayBuzz.asyncListeners.push({eventName:a,callback:b})},window.addEventListener("PlaybuzzScriptReady",function(){for(var a=0;a<PlayBuzz.asyncListeners.length;a++)PlayBuzz.on(PlayBuzz.asyncListeners[a].eventName,PlayBuzz.asyncListeners[a].callback)})}function b(){var a,b=document.location.search.indexOf("pbprefix")>=0?"stg-embed":"embed",c="playbuzz-sdk";document.getElementById(c)||(a=document.createElement("script"),a.id=c,a.src="https://"+b+".playbuzz.com/sdk.js",document.head.appendChild(a))}a(),b()}();