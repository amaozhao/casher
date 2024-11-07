import{L as t,M as e,N as n,o,f as r,w as i,y as s,z as a,m as u,i as l,e as c,J as h,j as d,t as f,b as g}from"./index-DI6-3tZP.js";import{_ as p,a as m,r as y,c as w}from"./home.BlDXPHWt.js";class C{constructor(e,n){this.options=e,this.animation=t({...e}),this.currentStepAnimates={},this.next=0,this.$=n}_nvuePushAnimates(t,e){let n=this.currentStepAnimates[this.next],o={};if(o=n||{styles:{},config:{}},E.includes(t)){o.styles.transform||(o.styles.transform="");let n="";"rotate"===t&&(n="deg"),o.styles.transform+=`${t}(${e+n}) `}else o.styles[t]=`${e}`;this.currentStepAnimates[this.next]=o}_animateRun(t={},e={}){let n=this.$.$refs.ani.ref;if(n)return new Promise(((o,r)=>{nvueAnimation.transition(n,{styles:t,...e},(t=>{o()}))}))}_nvueNextAnimate(t,e=0,n){let o=t[e];if(o){let{styles:r,config:i}=o;this._animateRun(r,i).then((()=>{e+=1,this._nvueNextAnimate(t,e,n)}))}else this.currentStepAnimates={},"function"==typeof n&&n(),this.isEnd=!0}step(t={}){return this.animation.step(t),this}run(t){this.$.animationData=this.animation.export(),this.$.timer=setTimeout((()=>{"function"==typeof t&&t()}),this.$.durationTime)}}const E=["matrix","matrix3d","rotate","rotate3d","rotateX","rotateY","rotateZ","scale","scale3d","scaleX","scaleY","scaleZ","skew","skewX","skewY","translate","translate3d","translateX","translateY","translateZ"];function b(t,e){if(e)return clearTimeout(e.timer),new C(t,e)}E.concat(["opacity","backgroundColor"],["width","height","left","right","top","bottom"]).forEach((t=>{C.prototype[t]=function(...e){return this.animation[t](...e),this}}));const T=p({name:"uniTransition",emits:["click","change"],props:{show:{type:Boolean,default:!1},modeClass:{type:[Array,String],default:()=>"fade"},duration:{type:Number,default:300},styles:{type:Object,default:()=>({})},customClass:{type:String,default:""},onceRender:{type:Boolean,default:!1}},data:()=>({isShow:!1,transform:"",opacity:1,animationData:{},durationTime:300,config:{}}),watch:{show:{handler(t){t?this.open():this.isShow&&this.close()},immediate:!0}},computed:{stylesObject(){let t={...this.styles,"transition-duration":this.duration/1e3+"s"},e="";for(let n in t){e+=this.toLine(n)+":"+t[n]+";"}return e},transformStyles(){return"transform:"+this.transform+";opacity:"+this.opacity+";"+this.stylesObject}},created(){this.config={duration:this.duration,timingFunction:"ease",transformOrigin:"50% 50%",delay:0},this.durationTime=this.duration},methods:{init(t={}){t.duration&&(this.durationTime=t.duration),this.animation=b(Object.assign(this.config,t),this)},onClick(){this.$emit("click",{detail:this.isShow})},step(t,e={}){if(this.animation){for(let e in t)try{"object"==typeof t[e]?this.animation[e](...t[e]):this.animation[e](t[e])}catch(n){console.error(`方法 ${e} 不存在`)}return this.animation.step(e),this}},run(t){this.animation&&this.animation.run(t)},open(){clearTimeout(this.timer),this.transform="",this.isShow=!0;let{opacity:t,transform:e}=this.styleInit(!1);void 0!==t&&(this.opacity=t),this.transform=e,this.$nextTick((()=>{this.timer=setTimeout((()=>{this.animation=b(this.config,this),this.tranfromInit(!1).step(),this.animation.run(),this.$emit("change",{detail:this.isShow})}),20)}))},close(t){this.animation&&this.tranfromInit(!0).step().run((()=>{this.isShow=!1,this.animationData=null,this.animation=null;let{opacity:t,transform:e}=this.styleInit(!1);this.opacity=t||1,this.transform=e,this.$emit("change",{detail:this.isShow})}))},styleInit(t){let e={transform:""},n=(t,n)=>{"fade"===n?e.opacity=this.animationType(t)[n]:e.transform+=this.animationType(t)[n]+" "};return"string"==typeof this.modeClass?n(t,this.modeClass):this.modeClass.forEach((e=>{n(t,e)})),e},tranfromInit(t){let e=(t,e)=>{let n=null;"fade"===e?n=t?0:1:(n=t?"-100%":"0","zoom-in"===e&&(n=t?.8:1),"zoom-out"===e&&(n=t?1.2:1),"slide-right"===e&&(n=t?"100%":"0"),"slide-bottom"===e&&(n=t?"100%":"0")),this.animation[this.animationMode()[e]](n)};return"string"==typeof this.modeClass?e(t,this.modeClass):this.modeClass.forEach((n=>{e(t,n)})),this.animation},animationType:t=>({fade:t?0:1,"slide-top":`translateY(${t?"0":"-100%"})`,"slide-right":`translateX(${t?"0":"100%"})`,"slide-bottom":`translateY(${t?"0":"100%"})`,"slide-left":`translateX(${t?"0":"-100%"})`,"zoom-in":`scaleX(${t?1:.8}) scaleY(${t?1:.8})`,"zoom-out":`scaleX(${t?1:1.2}) scaleY(${t?1:1.2})`}),animationMode:()=>({fade:"opacity","slide-top":"translateY","slide-right":"translateX","slide-bottom":"translateY","slide-left":"translateX","zoom-in":"scale","zoom-out":"scale"}),toLine:t=>t.replace(/([A-Z])/g,"-$1").toLowerCase()}},[["render",function(t,c,h,d,f,g){const p=l;return e((o(),r(p,{ref:"ani",animation:f.animationData,class:a(h.customClass),style:u(g.transformStyles),onClick:g.onClick},{default:i((()=>[s(t.$slots,"default")])),_:3},8,["animation","class","style","onClick"])),[[n,f.isShow]])}]]);const k=p({name:"uniPopup",components:{keypress:{name:"Keypress",props:{disable:{type:Boolean,default:!1}},mounted(){const t={esc:["Esc","Escape"],tab:"Tab",enter:"Enter",space:[" ","Spacebar"],up:["Up","ArrowUp"],left:["Left","ArrowLeft"],right:["Right","ArrowRight"],down:["Down","ArrowDown"],delete:["Backspace","Delete","Del"]};document.addEventListener("keyup",(e=>{if(this.disable)return;const n=Object.keys(t).find((n=>{const o=e.key,r=t[n];return r===o||Array.isArray(r)&&r.includes(o)}));n&&setTimeout((()=>{this.$emit(n,{})}),0)}))},render:()=>{}}},emits:["change","maskClick"],props:{animation:{type:Boolean,default:!0},type:{type:String,default:"center"},isMaskClick:{type:Boolean,default:null},maskClick:{type:Boolean,default:null},backgroundColor:{type:String,default:"none"},safeArea:{type:Boolean,default:!0},maskBackgroundColor:{type:String,default:"rgba(0, 0, 0, 0.4)"},borderRadius:{type:String}},watch:{type:{handler:function(t){this.config[t]&&this[this.config[t]](!0)},immediate:!0},isDesktop:{handler:function(t){this.config[t]&&this[this.config[this.type]](!0)},immediate:!0},maskClick:{handler:function(t){this.mkclick=t},immediate:!0},isMaskClick:{handler:function(t){this.mkclick=t},immediate:!0},showPopup(t){document.getElementsByTagName("body")[0].style.overflow=t?"hidden":"visible"}},data(){return{duration:300,ani:[],showPopup:!1,showTrans:!1,popupWidth:0,popupHeight:0,config:{top:"top",bottom:"bottom",center:"center",left:"left",right:"right",message:"top",dialog:"center",share:"bottom"},maskClass:{position:"fixed",bottom:0,top:0,left:0,right:0,backgroundColor:"rgba(0, 0, 0, 0.4)"},transClass:{backgroundColor:"transparent",borderRadius:this.borderRadius||"0",position:"fixed",left:0,right:0},maskShow:!0,mkclick:!0,popupstyle:"top"}},computed:{getStyles(){let t={backgroundColor:this.bg};return this.borderRadius,t=Object.assign(t,{borderRadius:this.borderRadius}),t},isDesktop(){return this.popupWidth>=500&&this.popupHeight>=500},bg(){return""===this.backgroundColor||"none"===this.backgroundColor?"transparent":this.backgroundColor}},mounted(){(()=>{const{windowWidth:t,windowHeight:e,windowTop:n,safeArea:o,screenHeight:r,safeAreaInsets:i}=g();this.popupWidth=t,this.popupHeight=e+(n||0),o&&this.safeArea?this.safeAreaInsets=i.bottom:this.safeAreaInsets=0})()},unmounted(){this.setH5Visible()},activated(){this.setH5Visible(!this.showPopup)},deactivated(){this.setH5Visible(!0)},created(){null===this.isMaskClick&&null===this.maskClick?this.mkclick=!0:this.mkclick=null!==this.isMaskClick?this.isMaskClick:this.maskClick,this.animation?this.duration=300:this.duration=0,this.messageChild=null,this.clearPropagation=!1,this.maskClass.backgroundColor=this.maskBackgroundColor},methods:{setH5Visible(t=!0){document.getElementsByTagName("body")[0].style.overflow=t?"visible":"hidden"},closeMask(){this.maskShow=!1},disableMask(){this.mkclick=!1},clear(t){t.stopPropagation(),this.clearPropagation=!0},open(t){if(this.showPopup)return;t&&-1!==["top","center","bottom","left","right","message","dialog","share"].indexOf(t)||(t=this.type),this.config[t]?(this[this.config[t]](),this.$emit("change",{show:!0,type:t})):console.error("缺少类型：",t)},close(t){this.showTrans=!1,this.$emit("change",{show:!1,type:this.type}),clearTimeout(this.timer),this.timer=setTimeout((()=>{this.showPopup=!1}),300)},touchstart(){this.clearPropagation=!1},onTap(){this.clearPropagation?this.clearPropagation=!1:(this.$emit("maskClick"),this.mkclick&&this.close())},top(t){this.popupstyle=this.isDesktop?"fixforpc-top":"top",this.ani=["slide-top"],this.transClass={position:"fixed",left:0,right:0,backgroundColor:this.bg,borderRadius:this.borderRadius||"0"},t||(this.showPopup=!0,this.showTrans=!0,this.$nextTick((()=>{this.messageChild&&"message"===this.type&&this.messageChild.timerClose()})))},bottom(t){this.popupstyle="bottom",this.ani=["slide-bottom"],this.transClass={position:"fixed",left:0,right:0,bottom:0,paddingBottom:this.safeAreaInsets+"px",backgroundColor:this.bg,borderRadius:this.borderRadius||"0"},t||(this.showPopup=!0,this.showTrans=!0)},center(t){this.popupstyle="center",this.ani=["zoom-out","fade"],this.transClass={position:"fixed",display:"flex",flexDirection:"column",bottom:0,left:0,right:0,top:0,justifyContent:"center",alignItems:"center",borderRadius:this.borderRadius||"0"},t||(this.showPopup=!0,this.showTrans=!0)},left(t){this.popupstyle="left",this.ani=["slide-left"],this.transClass={position:"fixed",left:0,bottom:0,top:0,backgroundColor:this.bg,borderRadius:this.borderRadius||"0",display:"flex",flexDirection:"column"},t||(this.showPopup=!0,this.showTrans=!0)},right(t){this.popupstyle="right",this.ani=["slide-right"],this.transClass={position:"fixed",bottom:0,right:0,top:0,backgroundColor:this.bg,borderRadius:this.borderRadius||"0",display:"flex",flexDirection:"column"},t||(this.showPopup=!0,this.showTrans=!0)}}},[["render",function(t,e,n,g,p,y){const w=m(c("uni-transition"),T),C=l,E=h("keypress");return p.showPopup?(o(),r(C,{key:0,class:a(["uni-popup",[p.popupstyle,y.isDesktop?"fixforpc-z-index":""]])},{default:i((()=>[d(C,{onTouchstart:y.touchstart},{default:i((()=>[p.maskShow?(o(),r(w,{key:"1",name:"mask","mode-class":"fade",styles:p.maskClass,duration:p.duration,show:p.showTrans,onClick:y.onTap},null,8,["styles","duration","show","onClick"])):f("",!0),d(w,{key:"2","mode-class":p.ani,name:"content",styles:p.transClass,duration:p.duration,show:p.showTrans,onClick:y.onTap},{default:i((()=>[d(C,{class:a(["uni-popup__wrapper",[p.popupstyle]]),style:u(y.getStyles),onClick:y.clear},{default:i((()=>[s(t.$slots,"default",{},void 0,!0)])),_:3},8,["style","class","onClick"])])),_:3},8,["mode-class","styles","duration","show","onClick"])])),_:3},8,["onTouchstart"]),p.maskShow?(o(),r(E,{key:0,onEsc:y.onTap},null,8,["onEsc"])):f("",!0)])),_:3},8,["class"])):f("",!0)}],["__scopeId","data-v-f0b957f8"]]);function A(t){return y.httpRequest({url:w.userInfo,method:"GET"},t)}function v(t){return y.httpRequest({url:w.getPower,method:"GET"},t)}function P(t){return y.httpRequest({url:w.powersOptions,method:"GET"},t)}function R(t){return y.httpRequest({url:w.clculatePrice,method:"POST"},t)}function B(t){return y.httpRequest({url:w.transactionsList,method:"GET"},t)}function I(t){return y.httpRequest({url:w.durationType,method:"GET"},t)}function M(t){return y.httpRequest({url:w.durationPrice,method:"POST"},t)}var N={},S={},x={};let L;const U=[0,26,44,70,100,134,172,196,242,292,346,404,466,532,581,655,733,815,901,991,1085,1156,1258,1364,1474,1588,1706,1828,1921,2051,2185,2323,2465,2611,2761,2876,3034,3196,3362,3532,3706];x.getSymbolSize=function(t){if(!t)throw new Error('"version" cannot be null or undefined');if(t<1||t>40)throw new Error('"version" should be in range from 1 to 40');return 4*t+17},x.getSymbolTotalCodewords=function(t){return U[t]},x.getBCHDigit=function(t){let e=0;for(;0!==t;)e++,t>>>=1;return e},x.setToSJISFunction=function(t){if("function"!=typeof t)throw new Error('"toSJISFunc" is not a valid function.');L=t},x.isKanjiModeEnabled=function(){return void 0!==L},x.toSJIS=function(t){return L(t)};var D,$={};function _(){this.buffer=[],this.length=0}(D=$).L={bit:1},D.M={bit:0},D.Q={bit:3},D.H={bit:2},D.isValid=function(t){return t&&void 0!==t.bit&&t.bit>=0&&t.bit<4},D.from=function(t,e){if(D.isValid(t))return t;try{return function(t){if("string"!=typeof t)throw new Error("Param is not a string");switch(t.toLowerCase()){case"l":case"low":return D.L;case"m":case"medium":return D.M;case"q":case"quartile":return D.Q;case"h":case"high":return D.H;default:throw new Error("Unknown EC Level: "+t)}}(t)}catch(n){return e}},_.prototype={get:function(t){const e=Math.floor(t/8);return 1==(this.buffer[e]>>>7-t%8&1)},put:function(t,e){for(let n=0;n<e;n++)this.putBit(1==(t>>>e-n-1&1))},getLengthInBits:function(){return this.length},putBit:function(t){const e=Math.floor(this.length/8);this.buffer.length<=e&&this.buffer.push(0),t&&(this.buffer[e]|=128>>>this.length%8),this.length++}};var z=_;function H(t){if(!t||t<1)throw new Error("BitMatrix size must be defined and greater than 0");this.size=t,this.data=new Uint8Array(t*t),this.reservedBit=new Uint8Array(t*t)}H.prototype.set=function(t,e,n,o){const r=t*this.size+e;this.data[r]=n,o&&(this.reservedBit[r]=!0)},H.prototype.get=function(t,e){return this.data[t*this.size+e]},H.prototype.xor=function(t,e,n){this.data[t*this.size+e]^=n},H.prototype.isReserved=function(t,e){return this.reservedBit[t*this.size+e]};var Y=H,q={};!function(t){const e=x.getSymbolSize;t.getRowColCoords=function(t){if(1===t)return[];const n=Math.floor(t/7)+2,o=e(t),r=145===o?26:2*Math.ceil((o-13)/(2*n-2)),i=[o-7];for(let e=1;e<n-1;e++)i[e]=i[e-1]-r;return i.push(6),i.reverse()},t.getPositions=function(e){const n=[],o=t.getRowColCoords(e),r=o.length;for(let t=0;t<r;t++)for(let e=0;e<r;e++)0===t&&0===e||0===t&&e===r-1||t===r-1&&0===e||n.push([o[t],o[e]]);return n}}(q);var O={};const F=x.getSymbolSize;O.getPositions=function(t){const e=F(t);return[[0,0],[e-7,0],[0,e-7]]};var j={};!function(t){t.Patterns={PATTERN000:0,PATTERN001:1,PATTERN010:2,PATTERN011:3,PATTERN100:4,PATTERN101:5,PATTERN110:6,PATTERN111:7};const e=3,n=3,o=40,r=10;function i(e,n,o){switch(e){case t.Patterns.PATTERN000:return(n+o)%2==0;case t.Patterns.PATTERN001:return n%2==0;case t.Patterns.PATTERN010:return o%3==0;case t.Patterns.PATTERN011:return(n+o)%3==0;case t.Patterns.PATTERN100:return(Math.floor(n/2)+Math.floor(o/3))%2==0;case t.Patterns.PATTERN101:return n*o%2+n*o%3==0;case t.Patterns.PATTERN110:return(n*o%2+n*o%3)%2==0;case t.Patterns.PATTERN111:return(n*o%3+(n+o)%2)%2==0;default:throw new Error("bad maskPattern:"+e)}}t.isValid=function(t){return null!=t&&""!==t&&!isNaN(t)&&t>=0&&t<=7},t.from=function(e){return t.isValid(e)?parseInt(e,10):void 0},t.getPenaltyN1=function(t){const n=t.size;let o=0,r=0,i=0,s=null,a=null;for(let u=0;u<n;u++){r=i=0,s=a=null;for(let l=0;l<n;l++){let n=t.get(u,l);n===s?r++:(r>=5&&(o+=e+(r-5)),s=n,r=1),n=t.get(l,u),n===a?i++:(i>=5&&(o+=e+(i-5)),a=n,i=1)}r>=5&&(o+=e+(r-5)),i>=5&&(o+=e+(i-5))}return o},t.getPenaltyN2=function(t){const e=t.size;let o=0;for(let n=0;n<e-1;n++)for(let r=0;r<e-1;r++){const e=t.get(n,r)+t.get(n,r+1)+t.get(n+1,r)+t.get(n+1,r+1);4!==e&&0!==e||o++}return o*n},t.getPenaltyN3=function(t){const e=t.size;let n=0,r=0,i=0;for(let o=0;o<e;o++){r=i=0;for(let s=0;s<e;s++)r=r<<1&2047|t.get(o,s),s>=10&&(1488===r||93===r)&&n++,i=i<<1&2047|t.get(s,o),s>=10&&(1488===i||93===i)&&n++}return n*o},t.getPenaltyN4=function(t){let e=0;const n=t.data.length;for(let o=0;o<n;o++)e+=t.data[o];return Math.abs(Math.ceil(100*e/n/5)-10)*r},t.applyMask=function(t,e){const n=e.size;for(let o=0;o<n;o++)for(let r=0;r<n;r++)e.isReserved(r,o)||e.xor(r,o,i(t,r,o))},t.getBestMask=function(e,n){const o=Object.keys(t.Patterns).length;let r=0,i=1/0;for(let s=0;s<o;s++){n(s),t.applyMask(s,e);const o=t.getPenaltyN1(e)+t.getPenaltyN2(e)+t.getPenaltyN3(e)+t.getPenaltyN4(e);t.applyMask(s,e),o<i&&(i=o,r=s)}return r}}(j);var J={};const K=$,V=[1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,4,1,2,4,4,2,4,4,4,2,4,6,5,2,4,6,6,2,5,8,8,4,5,8,8,4,5,8,11,4,8,10,11,4,9,12,16,4,9,16,16,6,10,12,18,6,10,17,16,6,11,16,19,6,13,18,21,7,14,21,25,8,16,20,25,8,17,23,25,9,17,23,34,9,18,25,30,10,20,27,32,12,21,29,35,12,23,34,37,12,25,34,40,13,26,35,42,14,28,38,45,15,29,40,48,16,31,43,51,17,33,45,54,18,35,48,57,19,37,51,60,19,38,53,63,20,40,56,66,21,43,59,70,22,45,62,74,24,47,65,77,25,49,68,81],X=[7,10,13,17,10,16,22,28,15,26,36,44,20,36,52,64,26,48,72,88,36,64,96,112,40,72,108,130,48,88,132,156,60,110,160,192,72,130,192,224,80,150,224,264,96,176,260,308,104,198,288,352,120,216,320,384,132,240,360,432,144,280,408,480,168,308,448,532,180,338,504,588,196,364,546,650,224,416,600,700,224,442,644,750,252,476,690,816,270,504,750,900,300,560,810,960,312,588,870,1050,336,644,952,1110,360,700,1020,1200,390,728,1050,1260,420,784,1140,1350,450,812,1200,1440,480,868,1290,1530,510,924,1350,1620,540,980,1440,1710,570,1036,1530,1800,570,1064,1590,1890,600,1120,1680,1980,630,1204,1770,2100,660,1260,1860,2220,720,1316,1950,2310,750,1372,2040,2430];J.getBlocksCount=function(t,e){switch(e){case K.L:return V[4*(t-1)+0];case K.M:return V[4*(t-1)+1];case K.Q:return V[4*(t-1)+2];case K.H:return V[4*(t-1)+3];default:return}},J.getTotalCodewordsCount=function(t,e){switch(e){case K.L:return X[4*(t-1)+0];case K.M:return X[4*(t-1)+1];case K.Q:return X[4*(t-1)+2];case K.H:return X[4*(t-1)+3];default:return}};var Q={},G={};const Z=new Uint8Array(512),W=new Uint8Array(256);!function(){let t=1;for(let e=0;e<255;e++)Z[e]=t,W[t]=e,t<<=1,256&t&&(t^=285);for(let e=255;e<512;e++)Z[e]=Z[e-255]}(),G.log=function(t){if(t<1)throw new Error("log("+t+")");return W[t]},G.exp=function(t){return Z[t]},G.mul=function(t,e){return 0===t||0===e?0:Z[W[t]+W[e]]},function(t){const e=G;t.mul=function(t,n){const o=new Uint8Array(t.length+n.length-1);for(let r=0;r<t.length;r++)for(let i=0;i<n.length;i++)o[r+i]^=e.mul(t[r],n[i]);return o},t.mod=function(t,n){let o=new Uint8Array(t);for(;o.length-n.length>=0;){const t=o[0];for(let i=0;i<n.length;i++)o[i]^=e.mul(n[i],t);let r=0;for(;r<o.length&&0===o[r];)r++;o=o.slice(r)}return o},t.generateECPolynomial=function(n){let o=new Uint8Array([1]);for(let r=0;r<n;r++)o=t.mul(o,new Uint8Array([1,e.exp(r)]));return o}}(Q);const tt=Q;function et(t){this.genPoly=void 0,this.degree=t,this.degree&&this.initialize(this.degree)}et.prototype.initialize=function(t){this.degree=t,this.genPoly=tt.generateECPolynomial(this.degree)},et.prototype.encode=function(t){if(!this.genPoly)throw new Error("Encoder not initialized");const e=new Uint8Array(t.length+this.degree);e.set(t);const n=tt.mod(e,this.genPoly),o=this.degree-n.length;if(o>0){const t=new Uint8Array(this.degree);return t.set(n,o),t}return n};var nt=et,ot={},rt={},it={isValid:function(t){return!isNaN(t)&&t>=1&&t<=40}},st={};let at="(?:[u3000-u303F]|[u3040-u309F]|[u30A0-u30FF]|[uFF00-uFFEF]|[u4E00-u9FAF]|[u2605-u2606]|[u2190-u2195]|u203B|[u2010u2015u2018u2019u2025u2026u201Cu201Du2225u2260]|[u0391-u0451]|[u00A7u00A8u00B1u00B4u00D7u00F7])+";at=at.replace(/u/g,"\\u");const ut="(?:(?![A-Z0-9 $%*+\\-./:]|"+at+")(?:.|[\r\n]))+";st.KANJI=new RegExp(at,"g"),st.BYTE_KANJI=new RegExp("[^A-Z0-9 $%*+\\-./:]+","g"),st.BYTE=new RegExp(ut,"g"),st.NUMERIC=new RegExp("[0-9]+","g"),st.ALPHANUMERIC=new RegExp("[A-Z $%*+\\-./:]+","g");const lt=new RegExp("^"+at+"$"),ct=new RegExp("^[0-9]+$"),ht=new RegExp("^[A-Z0-9 $%*+\\-./:]+$");st.testKanji=function(t){return lt.test(t)},st.testNumeric=function(t){return ct.test(t)},st.testAlphanumeric=function(t){return ht.test(t)},function(t){const e=it,n=st;t.NUMERIC={id:"Numeric",bit:1,ccBits:[10,12,14]},t.ALPHANUMERIC={id:"Alphanumeric",bit:2,ccBits:[9,11,13]},t.BYTE={id:"Byte",bit:4,ccBits:[8,16,16]},t.KANJI={id:"Kanji",bit:8,ccBits:[8,10,12]},t.MIXED={bit:-1},t.getCharCountIndicator=function(t,n){if(!t.ccBits)throw new Error("Invalid mode: "+t);if(!e.isValid(n))throw new Error("Invalid version: "+n);return n>=1&&n<10?t.ccBits[0]:n<27?t.ccBits[1]:t.ccBits[2]},t.getBestModeForData=function(e){return n.testNumeric(e)?t.NUMERIC:n.testAlphanumeric(e)?t.ALPHANUMERIC:n.testKanji(e)?t.KANJI:t.BYTE},t.toString=function(t){if(t&&t.id)return t.id;throw new Error("Invalid mode")},t.isValid=function(t){return t&&t.bit&&t.ccBits},t.from=function(e,n){if(t.isValid(e))return e;try{return function(e){if("string"!=typeof e)throw new Error("Param is not a string");switch(e.toLowerCase()){case"numeric":return t.NUMERIC;case"alphanumeric":return t.ALPHANUMERIC;case"kanji":return t.KANJI;case"byte":return t.BYTE;default:throw new Error("Unknown mode: "+e)}}(e)}catch(o){return n}}}(rt),function(t){const e=x,n=J,o=$,r=rt,i=it,s=e.getBCHDigit(7973);function a(t,e){return r.getCharCountIndicator(t,e)+4}function u(t,e){let n=0;return t.forEach((function(t){const o=a(t.mode,e);n+=o+t.getBitsLength()})),n}t.from=function(t,e){return i.isValid(t)?parseInt(t,10):e},t.getCapacity=function(t,o,s){if(!i.isValid(t))throw new Error("Invalid QR Code version");void 0===s&&(s=r.BYTE);const u=8*(e.getSymbolTotalCodewords(t)-n.getTotalCodewordsCount(t,o));if(s===r.MIXED)return u;const l=u-a(s,t);switch(s){case r.NUMERIC:return Math.floor(l/10*3);case r.ALPHANUMERIC:return Math.floor(l/11*2);case r.KANJI:return Math.floor(l/13);case r.BYTE:default:return Math.floor(l/8)}},t.getBestVersionForData=function(e,n){let i;const s=o.from(n,o.M);if(Array.isArray(e)){if(e.length>1)return function(e,n){for(let o=1;o<=40;o++)if(u(e,o)<=t.getCapacity(o,n,r.MIXED))return o}(e,s);if(0===e.length)return 1;i=e[0]}else i=e;return function(e,n,o){for(let r=1;r<=40;r++)if(n<=t.getCapacity(r,o,e))return r}(i.mode,i.getLength(),s)},t.getEncodedBits=function(t){if(!i.isValid(t)||t<7)throw new Error("Invalid QR Code version");let n=t<<12;for(;e.getBCHDigit(n)-s>=0;)n^=7973<<e.getBCHDigit(n)-s;return t<<12|n}}(ot);var dt={};const ft=x,gt=ft.getBCHDigit(1335);dt.getEncodedBits=function(t,e){const n=t.bit<<3|e;let o=n<<10;for(;ft.getBCHDigit(o)-gt>=0;)o^=1335<<ft.getBCHDigit(o)-gt;return 21522^(n<<10|o)};var pt={};const mt=rt;function yt(t){this.mode=mt.NUMERIC,this.data=t.toString()}yt.getBitsLength=function(t){return 10*Math.floor(t/3)+(t%3?t%3*3+1:0)},yt.prototype.getLength=function(){return this.data.length},yt.prototype.getBitsLength=function(){return yt.getBitsLength(this.data.length)},yt.prototype.write=function(t){let e,n,o;for(e=0;e+3<=this.data.length;e+=3)n=this.data.substr(e,3),o=parseInt(n,10),t.put(o,10);const r=this.data.length-e;r>0&&(n=this.data.substr(e),o=parseInt(n,10),t.put(o,3*r+1))};var wt=yt;const Ct=rt,Et=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","$","%","*","+","-",".","/",":"];function bt(t){this.mode=Ct.ALPHANUMERIC,this.data=t}bt.getBitsLength=function(t){return 11*Math.floor(t/2)+t%2*6},bt.prototype.getLength=function(){return this.data.length},bt.prototype.getBitsLength=function(){return bt.getBitsLength(this.data.length)},bt.prototype.write=function(t){let e;for(e=0;e+2<=this.data.length;e+=2){let n=45*Et.indexOf(this.data[e]);n+=Et.indexOf(this.data[e+1]),t.put(n,11)}this.data.length%2&&t.put(Et.indexOf(this.data[e]),6)};var Tt=bt;const kt=rt;function At(t){this.mode=kt.BYTE,this.data="string"==typeof t?(new TextEncoder).encode(t):new Uint8Array(t)}At.getBitsLength=function(t){return 8*t},At.prototype.getLength=function(){return this.data.length},At.prototype.getBitsLength=function(){return At.getBitsLength(this.data.length)},At.prototype.write=function(t){for(let e=0,n=this.data.length;e<n;e++)t.put(this.data[e],8)};var vt=At;const Pt=rt,Rt=x;function Bt(t){this.mode=Pt.KANJI,this.data=t}Bt.getBitsLength=function(t){return 13*t},Bt.prototype.getLength=function(){return this.data.length},Bt.prototype.getBitsLength=function(){return Bt.getBitsLength(this.data.length)},Bt.prototype.write=function(t){let e;for(e=0;e<this.data.length;e++){let n=Rt.toSJIS(this.data[e]);if(n>=33088&&n<=40956)n-=33088;else{if(!(n>=57408&&n<=60351))throw new Error("Invalid SJIS character: "+this.data[e]+"\nMake sure your charset is UTF-8");n-=49472}n=192*(n>>>8&255)+(255&n),t.put(n,13)}};var It,Mt=Bt,Nt={exports:{}},St=Nt.exports=It={single_source_shortest_paths:function(t,e,n){var o={},r={};r[e]=0;var i,s,a,u,l,c,h,d=It.PriorityQueue.make();for(d.push(e,0);!d.empty();)for(a in s=(i=d.pop()).value,u=i.cost,l=t[s]||{})l.hasOwnProperty(a)&&(c=u+l[a],h=r[a],(void 0===r[a]||h>c)&&(r[a]=c,d.push(a,c),o[a]=s));if(void 0!==n&&void 0===r[n]){var f=["Could not find a path from ",e," to ",n,"."].join("");throw new Error(f)}return o},extract_shortest_path_from_predecessor_list:function(t,e){for(var n=[],o=e;o;)n.push(o),t[o],o=t[o];return n.reverse(),n},find_path:function(t,e,n){var o=It.single_source_shortest_paths(t,e,n);return It.extract_shortest_path_from_predecessor_list(o,n)},PriorityQueue:{make:function(t){var e,n=It.PriorityQueue,o={};for(e in t=t||{},n)n.hasOwnProperty(e)&&(o[e]=n[e]);return o.queue=[],o.sorter=t.sorter||n.default_sorter,o},default_sorter:function(t,e){return t.cost-e.cost},push:function(t,e){var n={value:t,cost:e};this.queue.push(n),this.queue.sort(this.sorter)},pop:function(){return this.queue.shift()},empty:function(){return 0===this.queue.length}}};!function(t){const e=rt,n=wt,o=Tt,r=vt,i=Mt,s=st,a=x,u=St;function l(t){return unescape(encodeURIComponent(t)).length}function c(t,e,n){const o=[];let r;for(;null!==(r=t.exec(n));)o.push({data:r[0],index:r.index,mode:e,length:r[0].length});return o}function h(t){const n=c(s.NUMERIC,e.NUMERIC,t),o=c(s.ALPHANUMERIC,e.ALPHANUMERIC,t);let r,i;a.isKanjiModeEnabled()?(r=c(s.BYTE,e.BYTE,t),i=c(s.KANJI,e.KANJI,t)):(r=c(s.BYTE_KANJI,e.BYTE,t),i=[]);return n.concat(o,r,i).sort((function(t,e){return t.index-e.index})).map((function(t){return{data:t.data,mode:t.mode,length:t.length}}))}function d(t,s){switch(s){case e.NUMERIC:return n.getBitsLength(t);case e.ALPHANUMERIC:return o.getBitsLength(t);case e.KANJI:return i.getBitsLength(t);case e.BYTE:return r.getBitsLength(t)}}function f(t,s){let u;const l=e.getBestModeForData(t);if(u=e.from(s,l),u!==e.BYTE&&u.bit<l.bit)throw new Error('"'+t+'" cannot be encoded with mode '+e.toString(u)+".\n Suggested mode is: "+e.toString(l));switch(u!==e.KANJI||a.isKanjiModeEnabled()||(u=e.BYTE),u){case e.NUMERIC:return new n(t);case e.ALPHANUMERIC:return new o(t);case e.KANJI:return new i(t);case e.BYTE:return new r(t)}}t.fromArray=function(t){return t.reduce((function(t,e){return"string"==typeof e?t.push(f(e,null)):e.data&&t.push(f(e.data,e.mode)),t}),[])},t.fromString=function(n,o){const r=function(t){const n=[];for(let o=0;o<t.length;o++){const r=t[o];switch(r.mode){case e.NUMERIC:n.push([r,{data:r.data,mode:e.ALPHANUMERIC,length:r.length},{data:r.data,mode:e.BYTE,length:r.length}]);break;case e.ALPHANUMERIC:n.push([r,{data:r.data,mode:e.BYTE,length:r.length}]);break;case e.KANJI:n.push([r,{data:r.data,mode:e.BYTE,length:l(r.data)}]);break;case e.BYTE:n.push([{data:r.data,mode:e.BYTE,length:l(r.data)}])}}return n}(h(n,a.isKanjiModeEnabled())),i=function(t,n){const o={},r={start:{}};let i=["start"];for(let s=0;s<t.length;s++){const a=t[s],u=[];for(let t=0;t<a.length;t++){const l=a[t],c=""+s+t;u.push(c),o[c]={node:l,lastCount:0},r[c]={};for(let t=0;t<i.length;t++){const s=i[t];o[s]&&o[s].node.mode===l.mode?(r[s][c]=d(o[s].lastCount+l.length,l.mode)-d(o[s].lastCount,l.mode),o[s].lastCount+=l.length):(o[s]&&(o[s].lastCount=l.length),r[s][c]=d(l.length,l.mode)+4+e.getCharCountIndicator(l.mode,n))}}i=u}for(let e=0;e<i.length;e++)r[i[e]].end=0;return{map:r,table:o}}(r,o),s=u.find_path(i.map,"start","end"),c=[];for(let t=1;t<s.length-1;t++)c.push(i.table[s[t]].node);return t.fromArray(function(t){return t.reduce((function(t,e){const n=t.length-1>=0?t[t.length-1]:null;return n&&n.mode===e.mode?(t[t.length-1].data+=e.data,t):(t.push(e),t)}),[])}(c))},t.rawSplit=function(e){return t.fromArray(h(e,a.isKanjiModeEnabled()))}}(pt);const xt=x,Lt=$,Ut=z,Dt=Y,$t=q,_t=O,zt=j,Ht=J,Yt=nt,qt=ot,Ot=dt,Ft=rt,jt=pt;function Jt(t,e,n){const o=t.size,r=Ot.getEncodedBits(e,n);let i,s;for(i=0;i<15;i++)s=1==(r>>i&1),i<6?t.set(i,8,s,!0):i<8?t.set(i+1,8,s,!0):t.set(o-15+i,8,s,!0),i<8?t.set(8,o-i-1,s,!0):i<9?t.set(8,15-i-1+1,s,!0):t.set(8,15-i-1,s,!0);t.set(o-8,8,1,!0)}function Kt(t,e,n){const o=new Ut;n.forEach((function(e){o.put(e.mode.bit,4),o.put(e.getLength(),Ft.getCharCountIndicator(e.mode,t)),e.write(o)}));const r=8*(xt.getSymbolTotalCodewords(t)-Ht.getTotalCodewordsCount(t,e));for(o.getLengthInBits()+4<=r&&o.put(0,4);o.getLengthInBits()%8!=0;)o.putBit(0);const i=(r-o.getLengthInBits())/8;for(let s=0;s<i;s++)o.put(s%2?17:236,8);return function(t,e,n){const o=xt.getSymbolTotalCodewords(e),r=Ht.getTotalCodewordsCount(e,n),i=o-r,s=Ht.getBlocksCount(e,n),a=s-o%s,u=Math.floor(o/s),l=Math.floor(i/s),c=l+1,h=u-l,d=new Yt(h);let f=0;const g=new Array(s),p=new Array(s);let m=0;const y=new Uint8Array(t.buffer);for(let T=0;T<s;T++){const t=T<a?l:c;g[T]=y.slice(f,f+t),p[T]=d.encode(g[T]),f+=t,m=Math.max(m,t)}const w=new Uint8Array(o);let C,E,b=0;for(C=0;C<m;C++)for(E=0;E<s;E++)C<g[E].length&&(w[b++]=g[E][C]);for(C=0;C<h;C++)for(E=0;E<s;E++)w[b++]=p[E][C];return w}(o,t,e)}function Vt(t,e,n,o){let r;if(Array.isArray(t))r=jt.fromArray(t);else{if("string"!=typeof t)throw new Error("Invalid data");{let o=e;if(!o){const e=jt.rawSplit(t);o=qt.getBestVersionForData(e,n)}r=jt.fromString(t,o||40)}}const i=qt.getBestVersionForData(r,n);if(!i)throw new Error("The amount of data is too big to be stored in a QR Code");if(e){if(e<i)throw new Error("\nThe chosen QR Code version cannot contain this amount of data.\nMinimum version required to store current data is: "+i+".\n")}else e=i;const s=Kt(e,n,r),a=xt.getSymbolSize(e),u=new Dt(a);return function(t,e){const n=t.size,o=_t.getPositions(e);for(let r=0;r<o.length;r++){const e=o[r][0],i=o[r][1];for(let o=-1;o<=7;o++)if(!(e+o<=-1||n<=e+o))for(let r=-1;r<=7;r++)i+r<=-1||n<=i+r||(o>=0&&o<=6&&(0===r||6===r)||r>=0&&r<=6&&(0===o||6===o)||o>=2&&o<=4&&r>=2&&r<=4?t.set(e+o,i+r,!0,!0):t.set(e+o,i+r,!1,!0))}}(u,e),function(t){const e=t.size;for(let n=8;n<e-8;n++){const e=n%2==0;t.set(n,6,e,!0),t.set(6,n,e,!0)}}(u),function(t,e){const n=$t.getPositions(e);for(let o=0;o<n.length;o++){const e=n[o][0],r=n[o][1];for(let n=-2;n<=2;n++)for(let o=-2;o<=2;o++)-2===n||2===n||-2===o||2===o||0===n&&0===o?t.set(e+n,r+o,!0,!0):t.set(e+n,r+o,!1,!0)}}(u,e),Jt(u,n,0),e>=7&&function(t,e){const n=t.size,o=qt.getEncodedBits(e);let r,i,s;for(let a=0;a<18;a++)r=Math.floor(a/3),i=a%3+n-8-3,s=1==(o>>a&1),t.set(r,i,s,!0),t.set(i,r,s,!0)}(u,e),function(t,e){const n=t.size;let o=-1,r=n-1,i=7,s=0;for(let a=n-1;a>0;a-=2)for(6===a&&a--;;){for(let n=0;n<2;n++)if(!t.isReserved(r,a-n)){let o=!1;s<e.length&&(o=1==(e[s]>>>i&1)),t.set(r,a-n,o),i--,-1===i&&(s++,i=7)}if(r+=o,r<0||n<=r){r-=o,o=-o;break}}}(u,s),isNaN(o)&&(o=zt.getBestMask(u,Jt.bind(null,u,n))),zt.applyMask(o,u),Jt(u,n,o),{modules:u,version:e,errorCorrectionLevel:n,maskPattern:o,segments:r}}S.create=function(t,e){if(void 0===t||""===t)throw new Error("No input text");let n,o,r=Lt.M;return void 0!==e&&(r=Lt.from(e.errorCorrectionLevel,Lt.M),n=qt.from(e.version),o=zt.from(e.maskPattern),e.toSJISFunc&&xt.setToSJISFunction(e.toSJISFunc)),Vt(t,n,r,o)};var Xt={},Qt={};!function(t){function e(t){if("number"==typeof t&&(t=t.toString()),"string"!=typeof t)throw new Error("Color should be defined as hex string");let e=t.slice().replace("#","").split("");if(e.length<3||5===e.length||e.length>8)throw new Error("Invalid hex color: "+t);3!==e.length&&4!==e.length||(e=Array.prototype.concat.apply([],e.map((function(t){return[t,t]})))),6===e.length&&e.push("F","F");const n=parseInt(e.join(""),16);return{r:n>>24&255,g:n>>16&255,b:n>>8&255,a:255&n,hex:"#"+e.slice(0,6).join("")}}t.getOptions=function(t){t||(t={}),t.color||(t.color={});const n=void 0===t.margin||null===t.margin||t.margin<0?4:t.margin,o=t.width&&t.width>=21?t.width:void 0,r=t.scale||4;return{width:o,scale:o?4:r,margin:n,color:{dark:e(t.color.dark||"#000000ff"),light:e(t.color.light||"#ffffffff")},type:t.type,rendererOpts:t.rendererOpts||{}}},t.getScale=function(t,e){return e.width&&e.width>=t+2*e.margin?e.width/(t+2*e.margin):e.scale},t.getImageWidth=function(e,n){const o=t.getScale(e,n);return Math.floor((e+2*n.margin)*o)},t.qrToImageData=function(e,n,o){const r=n.modules.size,i=n.modules.data,s=t.getScale(r,o),a=Math.floor((r+2*o.margin)*s),u=o.margin*s,l=[o.color.light,o.color.dark];for(let t=0;t<a;t++)for(let n=0;n<a;n++){let c=4*(t*a+n),h=o.color.light;if(t>=u&&n>=u&&t<a-u&&n<a-u){h=l[i[Math.floor((t-u)/s)*r+Math.floor((n-u)/s)]?1:0]}e[c++]=h.r,e[c++]=h.g,e[c++]=h.b,e[c]=h.a}}}(Qt),function(t){const e=Qt;t.render=function(t,n,o){let r=o,i=n;void 0!==r||n&&n.getContext||(r=n,n=void 0),n||(i=function(){try{return document.createElement("canvas")}catch(t){throw new Error("You need to specify a canvas element")}}()),r=e.getOptions(r);const s=e.getImageWidth(t.modules.size,r),a=i.getContext("2d"),u=a.createImageData(s,s);return e.qrToImageData(u.data,t,r),function(t,e,n){t.clearRect(0,0,e.width,e.height),e.style||(e.style={}),e.height=n,e.width=n,e.style.height=n+"px",e.style.width=n+"px"}(a,i,s),a.putImageData(u,0,0),i},t.renderToDataURL=function(e,n,o){let r=o;void 0!==r||n&&n.getContext||(r=n,n=void 0),r||(r={});const i=t.render(e,n,r),s=r.type||"image/png",a=r.rendererOpts||{};return i.toDataURL(s,a.quality)}}(Xt);var Gt={};const Zt=Qt;function Wt(t,e){const n=t.a/255,o=e+'="'+t.hex+'"';return n<1?o+" "+e+'-opacity="'+n.toFixed(2).slice(1)+'"':o}function te(t,e,n){let o=t+e;return void 0!==n&&(o+=" "+n),o}Gt.render=function(t,e,n){const o=Zt.getOptions(e),r=t.modules.size,i=t.modules.data,s=r+2*o.margin,a=o.color.light.a?"<path "+Wt(o.color.light,"fill")+' d="M0 0h'+s+"v"+s+'H0z"/>':"",u="<path "+Wt(o.color.dark,"stroke")+' d="'+function(t,e,n){let o="",r=0,i=!1,s=0;for(let a=0;a<t.length;a++){const u=Math.floor(a%e),l=Math.floor(a/e);u||i||(i=!0),t[a]?(s++,a>0&&u>0&&t[a-1]||(o+=i?te("M",u+n,.5+l+n):te("m",r,0),r=0,i=!1),u+1<e&&t[a+1]||(o+=te("h",s),s=0)):r++}return o}(i,r,o.margin)+'"/>',l='viewBox="0 0 '+s+" "+s+'"',c='<svg xmlns="http://www.w3.org/2000/svg" '+(o.width?'width="'+o.width+'" height="'+o.width+'" ':"")+l+' shape-rendering="crispEdges">'+a+u+"</svg>\n";return"function"==typeof n&&n(null,c),c};const ee=function(){return"function"==typeof Promise&&Promise.prototype&&Promise.prototype.then},ne=S,oe=Xt,re=Gt;function ie(t,e,n,o,r){const i=[].slice.call(arguments,1),s=i.length,a="function"==typeof i[s-1];if(!a&&!ee())throw new Error("Callback required as last argument");if(!a){if(s<1)throw new Error("Too few arguments provided");return 1===s?(n=e,e=o=void 0):2!==s||e.getContext||(o=n,n=e,e=void 0),new Promise((function(r,i){try{const i=ne.create(n,o);r(t(i,e,o))}catch(s){i(s)}}))}if(s<2)throw new Error("Too few arguments provided");2===s?(r=n,n=e,e=o=void 0):3===s&&(e.getContext&&void 0===r?(r=o,o=void 0):(r=o,o=n,n=e,e=void 0));try{const i=ne.create(n,o);r(null,t(i,e,o))}catch(u){r(u)}}function se(t){return y.httpRequest({url:w.cappsList,method:"GET"},t)}function ae(t){return y.httpRequest({url:w.signStatus,method:"GET"},t)}function ue(t){return y.httpRequest({url:w.signPay,method:"POST"},t)}function le(t){return y.httpRequest({url:w.signUser,method:"POST"},t)}function ce(t){return y.httpRequest({url:w.templatesList,method:"GET"},t)}function he(t){return y.httpRequest({url:w.gpusList,method:"GET"},t)}function de(t){return y.httpRequest({url:w.createCapp,method:"POST"},t)}function fe(t){return y.httpRequest({url:w.startCapp+t,method:"POST"},t)}function ge(t){return y.httpRequest({url:w.stopCapp+t,method:"POST"},t)}function pe(t){return y.httpRequest({url:w.delCapp+t,method:"DELETE"},t)}N.create=ne.create,N.toCanvas=ie.bind(null,oe.render),N.toDataURL=ie.bind(null,oe.renderToDataURL),N.toString=ie.bind(null,(function(t,e,n){return re.render(t,n)}));export{k as _,ue as a,le as b,I as c,M as d,de as e,ce as f,v as g,he as h,R as i,se as j,fe as k,ge as l,pe as m,N as n,P as p,ae as s,B as t,A as u};
