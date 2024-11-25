import{L as t,M as s,N as i,o as e,c as o,w as a,r as n,n as r,A as l,f as h,v as c,u as d,a as p,d as u,J as m}from"./index-Cq5DkhQ_.js";import{_ as f}from"./http.ujTGAETh.js";function g(t,s){return"string"==typeof t?s:t}class y{constructor(s,i){this.options=s,this.animation=t({...s}),this.currentStepAnimates={},this.next=0,this.$=i}_nvuePushAnimates(t,s){let i=this.currentStepAnimates[this.next],e={};if(e=i||{styles:{},config:{}},k.includes(t)){e.styles.transform||(e.styles.transform="");let i="";"rotate"===t&&(i="deg"),e.styles.transform+=`${t}(${s+i}) `}else e.styles[t]=`${s}`;this.currentStepAnimates[this.next]=e}_animateRun(t={},s={}){let i=this.$.$refs.ani.ref;if(i)return new Promise(((e,o)=>{nvueAnimation.transition(i,{styles:t,...s},(t=>{e()}))}))}_nvueNextAnimate(t,s=0,i){let e=t[s];if(e){let{styles:o,config:a}=e;this._animateRun(o,a).then((()=>{s+=1,this._nvueNextAnimate(t,s,i)}))}else this.currentStepAnimates={},"function"==typeof i&&i(),this.isEnd=!0}step(t={}){return this.animation.step(t),this}run(t){this.$.animationData=this.animation.export(),this.$.timer=setTimeout((()=>{"function"==typeof t&&t()}),this.$.durationTime)}}const k=["matrix","matrix3d","rotate","rotate3d","rotateX","rotateY","rotateZ","scale","scale3d","scaleX","scaleY","scaleZ","skew","skewX","skewY","translate","translate3d","translateX","translateY","translateZ"];function C(t,s){if(s)return clearTimeout(s.timer),new y(t,s)}k.concat(["opacity","backgroundColor"],["width","height","left","right","top","bottom"]).forEach((t=>{y.prototype[t]=function(...s){return this.animation[t](...s),this}}));const b=f({name:"uniTransition",emits:["click","change"],props:{show:{type:Boolean,default:!1},modeClass:{type:[Array,String],default:()=>"fade"},duration:{type:Number,default:300},styles:{type:Object,default:()=>({})},customClass:{type:String,default:""},onceRender:{type:Boolean,default:!1}},data:()=>({isShow:!1,transform:"",opacity:1,animationData:{},durationTime:300,config:{}}),watch:{show:{handler(t){t?this.open():this.isShow&&this.close()},immediate:!0}},computed:{stylesObject(){let t={...this.styles,"transition-duration":this.duration/1e3+"s"},s="";for(let i in t){s+=this.toLine(i)+":"+t[i]+";"}return s},transformStyles(){return"transform:"+this.transform+";opacity:"+this.opacity+";"+this.stylesObject}},created(){this.config={duration:this.duration,timingFunction:"ease",transformOrigin:"50% 50%",delay:0},this.durationTime=this.duration},methods:{init(t={}){t.duration&&(this.durationTime=t.duration),this.animation=C(Object.assign(this.config,t),this)},onClick(){this.$emit("click",{detail:this.isShow})},step(t,s={}){if(this.animation){for(let s in t)try{"object"==typeof t[s]?this.animation[s](...t[s]):this.animation[s](t[s])}catch(i){console.error(`方法 ${s} 不存在`)}return this.animation.step(s),this}},run(t){this.animation&&this.animation.run(t)},open(){clearTimeout(this.timer),this.transform="",this.isShow=!0;let{opacity:t,transform:s}=this.styleInit(!1);void 0!==t&&(this.opacity=t),this.transform=s,this.$nextTick((()=>{this.timer=setTimeout((()=>{this.animation=C(this.config,this),this.tranfromInit(!1).step(),this.animation.run(),this.$emit("change",{detail:this.isShow})}),20)}))},close(t){this.animation&&this.tranfromInit(!0).step().run((()=>{this.isShow=!1,this.animationData=null,this.animation=null;let{opacity:t,transform:s}=this.styleInit(!1);this.opacity=t||1,this.transform=s,this.$emit("change",{detail:this.isShow})}))},styleInit(t){let s={transform:""},i=(t,i)=>{"fade"===i?s.opacity=this.animationType(t)[i]:s.transform+=this.animationType(t)[i]+" "};return"string"==typeof this.modeClass?i(t,this.modeClass):this.modeClass.forEach((s=>{i(t,s)})),s},tranfromInit(t){let s=(t,s)=>{let i=null;"fade"===s?i=t?0:1:(i=t?"-100%":"0","zoom-in"===s&&(i=t?.8:1),"zoom-out"===s&&(i=t?1.2:1),"slide-right"===s&&(i=t?"100%":"0"),"slide-bottom"===s&&(i=t?"100%":"0")),this.animation[this.animationMode()[s]](i)};return"string"==typeof this.modeClass?s(t,this.modeClass):this.modeClass.forEach((i=>{s(t,i)})),this.animation},animationType:t=>({fade:t?0:1,"slide-top":`translateY(${t?"0":"-100%"})`,"slide-right":`translateX(${t?"0":"100%"})`,"slide-bottom":`translateY(${t?"0":"100%"})`,"slide-left":`translateX(${t?"0":"-100%"})`,"zoom-in":`scaleX(${t?1:.8}) scaleY(${t?1:.8})`,"zoom-out":`scaleX(${t?1:1.2}) scaleY(${t?1:1.2})`}),animationMode:()=>({fade:"opacity","slide-top":"translateY","slide-right":"translateX","slide-bottom":"translateY","slide-left":"translateX","zoom-in":"scale","zoom-out":"scale"}),toLine:t=>t.replace(/([A-Z])/g,"-$1").toLowerCase()}},[["render",function(t,c,d,p,u,m){const f=h;return s((e(),o(f,{ref:"ani",animation:u.animationData,class:r(d.customClass),style:l(m.transformStyles),onClick:m.onClick},{default:a((()=>[n(t.$slots,"default")])),_:3},8,["animation","class","style","onClick"])),[[i,u.isShow]])}]]);const w=f({name:"uniPopup",components:{keypress:{name:"Keypress",props:{disable:{type:Boolean,default:!1}},mounted(){const t={esc:["Esc","Escape"],tab:"Tab",enter:"Enter",space:[" ","Spacebar"],up:["Up","ArrowUp"],left:["Left","ArrowLeft"],right:["Right","ArrowRight"],down:["Down","ArrowDown"],delete:["Backspace","Delete","Del"]};document.addEventListener("keyup",(s=>{if(this.disable)return;const i=Object.keys(t).find((i=>{const e=s.key,o=t[i];return o===e||Array.isArray(o)&&o.includes(e)}));i&&setTimeout((()=>{this.$emit(i,{})}),0)}))},render:()=>{}}},emits:["change","maskClick"],props:{animation:{type:Boolean,default:!0},type:{type:String,default:"center"},isMaskClick:{type:Boolean,default:null},maskClick:{type:Boolean,default:null},backgroundColor:{type:String,default:"none"},safeArea:{type:Boolean,default:!0},maskBackgroundColor:{type:String,default:"rgba(0, 0, 0, 0.4)"},borderRadius:{type:String}},watch:{type:{handler:function(t){this.config[t]&&this[this.config[t]](!0)},immediate:!0},isDesktop:{handler:function(t){this.config[t]&&this[this.config[this.type]](!0)},immediate:!0},maskClick:{handler:function(t){this.mkclick=t},immediate:!0},isMaskClick:{handler:function(t){this.mkclick=t},immediate:!0},showPopup(t){document.getElementsByTagName("body")[0].style.overflow=t?"hidden":"visible"}},data(){return{duration:300,ani:[],showPopup:!1,showTrans:!1,popupWidth:0,popupHeight:0,config:{top:"top",bottom:"bottom",center:"center",left:"left",right:"right",message:"top",dialog:"center",share:"bottom"},maskClass:{position:"fixed",bottom:0,top:0,left:0,right:0,backgroundColor:"rgba(0, 0, 0, 0.4)"},transClass:{backgroundColor:"transparent",borderRadius:this.borderRadius||"0",position:"fixed",left:0,right:0},maskShow:!0,mkclick:!0,popupstyle:"top"}},computed:{getStyles(){let t={backgroundColor:this.bg};return this.borderRadius,t=Object.assign(t,{borderRadius:this.borderRadius}),t},isDesktop(){return this.popupWidth>=500&&this.popupHeight>=500},bg(){return""===this.backgroundColor||"none"===this.backgroundColor?"transparent":this.backgroundColor}},mounted(){(()=>{const{windowWidth:t,windowHeight:s,windowTop:i,safeArea:e,screenHeight:o,safeAreaInsets:a}=m();this.popupWidth=t,this.popupHeight=s+(i||0),e&&this.safeArea?this.safeAreaInsets=a.bottom:this.safeAreaInsets=0})()},unmounted(){this.setH5Visible()},activated(){this.setH5Visible(!this.showPopup)},deactivated(){this.setH5Visible(!0)},created(){null===this.isMaskClick&&null===this.maskClick?this.mkclick=!0:this.mkclick=null!==this.isMaskClick?this.isMaskClick:this.maskClick,this.animation?this.duration=300:this.duration=0,this.messageChild=null,this.clearPropagation=!1,this.maskClass.backgroundColor=this.maskBackgroundColor},methods:{setH5Visible(t=!0){document.getElementsByTagName("body")[0].style.overflow=t?"visible":"hidden"},closeMask(){this.maskShow=!1},disableMask(){this.mkclick=!1},clear(t){t.stopPropagation(),this.clearPropagation=!0},open(t){if(this.showPopup)return;t&&-1!==["top","center","bottom","left","right","message","dialog","share"].indexOf(t)||(t=this.type),this.config[t]?(this[this.config[t]](),this.$emit("change",{show:!0,type:t})):console.error("缺少类型：",t)},close(t){this.showTrans=!1,this.$emit("change",{show:!1,type:this.type}),clearTimeout(this.timer),this.timer=setTimeout((()=>{this.showPopup=!1}),300)},touchstart(){this.clearPropagation=!1},onTap(){this.clearPropagation?this.clearPropagation=!1:(this.$emit("maskClick"),this.mkclick&&this.close())},top(t){this.popupstyle=this.isDesktop?"fixforpc-top":"top",this.ani=["slide-top"],this.transClass={position:"fixed",left:0,right:0,backgroundColor:this.bg,borderRadius:this.borderRadius||"0"},t||(this.showPopup=!0,this.showTrans=!0,this.$nextTick((()=>{this.messageChild&&"message"===this.type&&this.messageChild.timerClose()})))},bottom(t){this.popupstyle="bottom",this.ani=["slide-bottom"],this.transClass={position:"fixed",left:0,right:0,bottom:0,paddingBottom:this.safeAreaInsets+"px",backgroundColor:this.bg,borderRadius:this.borderRadius||"0"},t||(this.showPopup=!0,this.showTrans=!0)},center(t){this.popupstyle="center",this.ani=["zoom-out","fade"],this.transClass={position:"fixed",display:"flex",flexDirection:"column",bottom:0,left:0,right:0,top:0,justifyContent:"center",alignItems:"center",borderRadius:this.borderRadius||"0"},t||(this.showPopup=!0,this.showTrans=!0)},left(t){this.popupstyle="left",this.ani=["slide-left"],this.transClass={position:"fixed",left:0,bottom:0,top:0,backgroundColor:this.bg,borderRadius:this.borderRadius||"0",display:"flex",flexDirection:"column"},t||(this.showPopup=!0,this.showTrans=!0)},right(t){this.popupstyle="right",this.ani=["slide-right"],this.transClass={position:"fixed",bottom:0,right:0,top:0,backgroundColor:this.bg,borderRadius:this.borderRadius||"0",display:"flex",flexDirection:"column"},t||(this.showPopup=!0,this.showTrans=!0)}}},[["render",function(t,s,i,m,f,y){const k=g(c("uni-transition"),b),C=h,w=d("keypress");return f.showPopup?(e(),o(C,{key:0,class:r(["uni-popup",[f.popupstyle,y.isDesktop?"fixforpc-z-index":""]])},{default:a((()=>[p(C,{onTouchstart:y.touchstart},{default:a((()=>[f.maskShow?(e(),o(k,{key:"1",name:"mask","mode-class":"fade",styles:f.maskClass,duration:f.duration,show:f.showTrans,onClick:y.onTap},null,8,["styles","duration","show","onClick"])):u("",!0),p(k,{key:"2","mode-class":f.ani,name:"content",styles:f.transClass,duration:f.duration,show:f.showTrans,onClick:y.onTap},{default:a((()=>[p(C,{class:r(["uni-popup__wrapper",[f.popupstyle]]),style:l(y.getStyles),onClick:y.clear},{default:a((()=>[n(t.$slots,"default",{},void 0,!0)])),_:3},8,["style","class","onClick"])])),_:3},8,["mode-class","styles","duration","show","onClick"])])),_:3},8,["onTouchstart"]),f.maskShow?(e(),o(w,{key:0,onEsc:y.onTap},null,8,["onEsc"])):u("",!0)])),_:3},8,["class"])):u("",!0)}],["__scopeId","data-v-f0b957f8"]]),T="data:image/svg+xml,%3csvg%20width='24'%20height='24'%20viewBox='0%200%2024%2024'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M8.46949%2015.7265C9.63148%2016.9075%209.76599%2018.177%208.47799%2019.486C7.67999%2020.2965%206.38798%2020.7835%204.60998%2020.992C4.51798%2021.003%204.42499%2021.0025%204.33248%2020.9915C3.70748%2020.9155%203.25099%2020.36%203.28099%2019.7255L3.28748%2019.6425L3.31298%2019.4325C3.53098%2017.7375%204.00299%2016.4965%204.76949%2015.7175C6.05749%2014.409%207.30698%2014.546%208.46949%2015.7265ZM19.115%203.31998L19.316%203.38148L19.5125%203.44698C19.7544%203.53178%2019.9737%203.67054%2020.154%203.85272C20.3343%204.0349%2020.4707%204.25574%2020.553%204.49848C21.3365%206.78748%2021.0875%209.10648%2019.8245%2011.4055C19.304%2012.3525%2018.638%2013.249%2017.8275%2014.0945L17.603%2014.324L17.3905%2014.532L17.3845%2014.5965C17.237%2015.9735%2016.1925%2017.7945%2014.268%2020.149L14.101%2020.3525L13.7935%2020.72C13.4455%2021.133%2012.7975%2021.018%2012.5945%2020.53L12.5705%2020.4645L11.4945%2017.0305L11.397%2016.963C10.7924%2016.5323%2010.2165%2016.0626%209.67299%2015.557L9.40549%2015.302L9.14349%2015.042C8.36961%2014.2545%207.67308%2013.3945%207.06349%2012.474L7.00399%2012.3815L3.49998%2011.2485C3.00698%2011.0885%202.84799%2010.479%203.16099%2010.096L3.20249%2010.049L3.24748%2010.007C6.12948%207.48898%208.25599%206.24048%209.77899%206.34448L9.87699%206.35298L9.93399%206.35998L10.0625%206.22998C10.7535%205.54298%2011.477%204.95848%2012.2335%204.47798L12.4865%204.32148L12.719%204.18548C14.83%202.98848%2016.973%202.69398%2019.115%203.32048V3.31998ZM12.6555%208.15548C11.779%209.03248%2011.782%2010.457%2012.6625%2011.3375C13.543%2012.218%2014.9675%2012.221%2015.8445%2011.3445C16.721%2010.4675%2016.718%209.04298%2015.8375%208.16248C14.957%207.28198%2013.5325%207.27898%2012.6555%208.15548Z'%20fill='%23FFE70B'/%3e%3c/svg%3e";export{w as _,T as a,g as r};
