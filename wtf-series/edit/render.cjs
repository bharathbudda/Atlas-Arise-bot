// usage: node render.js <ep> <startFrame> <endFrame> [times...]   (times mode if 3rd arg is 'T')
const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{const [ep,a,b,...rest]=process.argv.slice(2);
 const tl=JSON.parse(fs.readFileSync(path.join(__dirname,'build',ep,'timeline.json')));
 const out=path.join(__dirname,'build',ep,'frames'); fs.mkdirSync(out,{recursive:true});
 const br=await chromium.launch(); const p=await br.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.join(__dirname,'engine.html')); await p.waitForTimeout(400);
 await p.evaluate(t=>window.init(t),tl);
 if(a==='T'){ for(const t of [b,...rest]){await p.evaluate(x=>window.render(x),parseFloat(t));await p.screenshot({path:path.join(out,`t_${t}.jpg`),type:'jpeg',quality:88});} }
 else { for(let i=parseInt(a);i<parseInt(b);i++){await p.evaluate(x=>window.render(x),i/30);await p.screenshot({path:path.join(out,String(i).padStart(5,'0')+'.jpg'),type:'jpeg',quality:92});} }
 await br.close();})();
