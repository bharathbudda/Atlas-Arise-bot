const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:2000}});
await p.goto('file://'+path.join(__dirname,'covers.html'));await p.waitForTimeout(800);
for(let i=1;i<=6;i++){const el=await p.$('#c'+i);await el.screenshot({path:path.join(__dirname,'..','out','covers',`WTF_EP0${i}_cover.jpg`),type:'jpeg',quality:92});}
await b.close();})();
