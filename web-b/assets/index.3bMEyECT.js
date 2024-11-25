import{b as e,c as t,a as s,h as a,d as o,r,e as i,o as n,p,j as c,w as l,k as u,t as d,x as h,F as m,q as w,i as _,I as f,v as g,f as y,y as P}from"./index-CTstRlDA.js";import{r as C,_ as b}from"./index.D-kQrq1M.js";import{p as I,a as x,g as v,b as k,d as T,w as D,_ as $}from"./check.BGT4OgCv.js";import{_ as L}from"./_plugin-vue_export-helper.BCo6x5W8.js";const S=L({props:{params:{type:Object,default:()=>({})}},data:()=>({account:null,powersID:null,powersList:[],powerValue:null,currencySum:null,qrCodeBase64:"",popupType:"bottom",second:30,start:!0,timer:null}),onShow:function(){},watch:{powerValue(e){this.getPricePowers()}},methods:{getPricePowers(){I({amount:Number(this.powerValue)}).then((e=>{2e4==e.code&&(this.currencySum=e.data.currency)}))},goProductPage(){e().windowWidth,this.popupType=e().windowWidth<768?"bottom":"center",this.$refs.popup.open(this.popupType),this.getUserPower(),this.getPowersOptions()},getPowersOptions(){x().then((e=>{2e4==e.code&&(this.powersList=e.data.PowerPurchaseOptions,this.powersID=this.powersList[0].ID,this.powerValue=this.powersList[0].PowerAmount)}))},changePower(e){this.powersID=e.ID,this.powerValue=e.PowerAmount},getUserPower(){v().then((e=>{2e4==e.code&&(this.account=e.data.account)}))},async createQRCode(e){try{this.qrCodeBase64=await k.toDataURL(e),this.$refs.popupcenter.open("center")}catch(t){console.error("生成二维码失败:",t)}},getUserInfo(){userInfo().then((e=>{2e4==e.code&&(this.userInfo=e.data.userInfo)}))},skewChange(e){this.getTransactionsList(),this.skewIndex=e},getTransactionsList(){transactionsList().then((e=>{2e4==e.code&&(this.depositList=e.data.transactions.Deposit||[],this.withdrawList=e.data.transactions.Withdraw||[])}))},handleWePay(){this.clearTimer(),t({title:"加载中",mask:!0}),s("isChinese");let e="";switch(s("uniPlatform")){case"mp-weixin":e="mp-weixin";break;case"web":e="wechat"}e=s("isChinese")?"wechat":"stripe";let i={amount:this.powerValue,payment_method:e,currency:"CNY"};T(i).then((e=>{if(2e4==e.code)if(a(),s("isChinese"))switch(s("uniPlatform")){case"mp-weixin":uni.requestPayment({provider:"wxpay",timeStamp:e.data.timeStamp,nonceStr:e.data.nonceStr,package:"prepay_id="+e.data.prepayid,signType:e.data.signType,paySign:e.data.paySign,success:function(e){o({icon:"success",title:"支付成功"}),r({url:"/pages/web/web18GpuProduct"})},fail:function(e){console.log("fail:"+JSON.stringify(e)),o({icon:"error",title:"支付失败"})}});break;case"web":this.createQRCode(e.data.url),this.getResult(e.data.id)}else window.location.href=e.data.url;else a()}))},getResult(e){this.timer=setInterval((()=>{this.second>0&&(this.second--,D(e).then((e=>{2e4==e.code&&"completed"==e.data.transaction.status&&(this.start=!1,o({icon:"success",title:"支付成功！"}),this.$refs.popupcenter.close(),this.$refs.popup.close(),this.getUserPower())})),(this.second<1||!this.start)&&(this.start=!1,o({icon:"none",title:"支付失败！"}),this.$refs.popupcenter.close(),this.clearTimer()))}),1e3)},clearTimer(){this.timer&&(clearInterval(this.timer),this.timer=null)}},beforeUnmount(){this.clearTimer()}},[["render",function(e,t,s,a,o,r){const I=_,x=f,v=g,k=C(i("uni-popup"),b);return n(),p(m,null,[c(k,{ref:"popup",type:o.popupType,class:"popupDiv"},{default:l((()=>[c(I,{id:"formDom",style:{"background-color":"aliceblue"}}),c(I,{class:"flex column alignCenter pop_div"},{default:l((()=>[c(I,{class:"pop_header_div"},{default:l((()=>[c(I,{class:"pop_header_text"},{default:l((()=>[u(d(e.$t("14_Top_up")),1)])),_:1})])),_:1}),c(I,{class:"pop_header_label"},{default:l((()=>[u(d(e.$t("14_remaining_power"))+" ",1),h("span",{class:"pop_header_value"},d(o.account),1)])),_:1}),c(I,{class:"flex row justifyCenter pop_item_div"},{default:l((()=>[(n(!0),p(m,null,w(o.powersList,((t,s)=>(n(),y(I,{class:P(["flex row justifyBetween alignCenter pop_item",o.powersID==t.ID?"pop_item_selected":""]),key:t.ID,onClick:e=>r.changePower(t)},{default:l((()=>[c(I,{class:"flex column justifyCenter alignCenter"},{default:l((()=>[c(I,{class:"pop_item_value"},{default:l((()=>[u(d(t.PowerAmount),1)])),_:2},1024),c(I,{class:"pop_item_label"},{default:l((()=>[u(d(e.$t("14_Computing_power")),1)])),_:1})])),_:2},1024),c(I,{class:"pop_item_money"},{default:l((()=>[u("¥"+d(t.AmountInCurrency),1)])),_:2},1024)])),_:2},1032,["class","onClick"])))),128))])),_:1}),c(x,{class:"custome_input",type:"number",placeholder:e.$t("14_Customize"),modelValue:o.powerValue,"onUpdate:modelValue":t[0]||(t[0]=e=>o.powerValue=e)},null,8,["placeholder","modelValue"]),c(I,{class:"pay_btn",onClick:t[1]||(t[1]=e=>r.handleWePay())},{default:l((()=>[u("¥"+d(o.currencySum)+" "+d(e.$t("14_Pay_now")),1)])),_:1}),c(I,{class:"flex row alignCenter agreement_div"},{default:l((()=>[c(v,{class:"btn_img",src:$}),c(I,{class:"agreement_text"},{default:l((()=>[u(d(e.$t("14_agree"))+" ",1),h("span",{class:"agreement_value"},d(e.$t("14_Agreement")),1)])),_:1})])),_:1})])),_:1})])),_:1},8,["type"]),c(k,{ref:"popupcenter",type:"center",animation:!1},{default:l((()=>[c(v,{src:o.qrCodeBase64,mode:"aspectFit"},null,8,["src"])])),_:1},512)],64)}],["__scopeId","data-v-e6d6d3c0"]]);export{S as P};
