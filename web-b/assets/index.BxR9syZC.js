import{b as e,c as t,a as s,h as a,d as o,r,e as i,o as n,p,j as l,w as c,k as u,v as d,x as h,F as m,q as w,i as _,I as f,u as g,f as y,z as P}from"./index-DZZGyAJD.js";import{q as C,j as v,r as x,_ as b}from"./index.B6uA7zyi.js";import{r as I}from"./uni-app.es.CjVRXCaX.js";import{r as k,c as T}from"./home.BwDbU5G1.js";import{_ as L}from"./_plugin-vue_export-helper.BCo6x5W8.js";const S="data:image/svg+xml,%3csvg%20width='18'%20height='18'%20viewBox='0%200%2018%2018'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M0%209C0%204.02944%204.02944%200%209%200C13.9706%200%2018%204.02944%2018%209C18%2013.9706%2013.9706%2018%209%2018C4.02944%2018%200%2013.9706%200%209Z'%20fill='%23019083'/%3e%3cpath%20d='M5%208.90909L7.66742%2011.8182L13%206'%20stroke='white'%20stroke-width='1.5'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3c/svg%3e";const j=L({props:{params:{type:Object,default:()=>({})}},data:()=>({account:null,powersID:null,powersList:[],powerValue:null,currencySum:null,qrCodeBase64:"",popupType:"bottom",second:30,start:!0,timer:null}),onShow:function(){},watch:{powerValue(e){this.getPricePowers()}},methods:{getPricePowers(){var e;(e={amount:Number(this.powerValue)},k.httpRequest({url:T.pricePowers,method:"POST"},e)).then((e=>{2e4==e.code&&(this.currencySum=e.data.currency)}))},goProductPage(){e().windowWidth,this.popupType=e().windowWidth<768?"bottom":"center",this.$refs.popup.open(this.popupType),this.getUserPower(),this.getPowersOptions()},getPowersOptions(){C().then((e=>{2e4==e.code&&(this.powersList=e.data.PowerPurchaseOptions,this.powersID=this.powersList[0].ID,this.powerValue=this.powersList[0].PowerAmount)}))},changePower(e){this.powersID=e.ID,this.powerValue=e.PowerAmount},getUserPower(){v().then((e=>{2e4==e.code&&(this.account=e.data.account)}))},async createQRCode(e){try{this.qrCodeBase64=await x.toDataURL(e),this.$refs.popupcenter.open("center")}catch(t){console.error("生成二维码失败:",t)}},getUserInfo(){userInfo().then((e=>{2e4==e.code&&(this.userInfo=e.data.userInfo)}))},skewChange(e){this.getTransactionsList(),this.skewIndex=e},getTransactionsList(){transactionsList().then((e=>{2e4==e.code&&(this.depositList=e.data.transactions.Deposit||[],this.withdrawList=e.data.transactions.Withdraw||[])}))},handleWePay(){this.clearTimer(),t({title:"加载中",mask:!0}),s("isChinese");let e="";switch(s("uniPlatform")){case"mp-weixin":e="mp-weixin";break;case"web":e="wechat"}e=s("isChinese")?"wechat":"stripe";let i={amount:this.powerValue,payment_method:e,currency:"CNY"};var n;(n=i,k.httpRequest({url:T.depositPay,method:"POST"},n)).then((e=>{if(2e4==e.code)if(a(),s("isChinese"))switch(s("uniPlatform")){case"mp-weixin":uni.requestPayment({provider:"wxpay",timeStamp:e.data.timeStamp,nonceStr:e.data.nonceStr,package:"prepay_id="+e.data.prepayid,signType:e.data.signType,paySign:e.data.paySign,success:function(e){o({icon:"success",title:"支付成功"}),r({url:"/pages/web/web18GpuProduct"})},fail:function(e){console.log("fail:"+JSON.stringify(e)),o({icon:"error",title:"支付失败"})}});break;case"web":this.createQRCode(e.data.url),this.getResult(e.data.id)}else window.location.href=e.data.url;else a()}))},getResult(e){this.timer=setInterval((()=>{var t;this.second>0&&(this.second--,(t=e,k.httpRequest({url:T.wechatPay+t,method:"GET"},t)).then((e=>{2e4==e.code&&"completed"==e.data.transaction.status&&(this.start=!1,o({icon:"success",title:"支付成功！"}),this.$refs.popupcenter.close(),this.$refs.popup.close(),this.getUserPower())})),(this.second<1||!this.start)&&(this.start=!1,o({icon:"none",title:"支付失败！"}),this.$refs.popupcenter.close(),this.clearTimer()))}),1e3)},clearTimer(){this.timer&&(clearInterval(this.timer),this.timer=null)}},beforeUnmount(){this.clearTimer()}},[["render",function(e,t,s,a,o,r){const C=_,v=f,x=g,k=I(i("uni-popup"),b);return n(),p(m,null,[l(k,{ref:"popup",type:o.popupType,class:"popupDiv"},{default:c((()=>[l(C,{id:"formDom",style:{"background-color":"aliceblue"}}),l(C,{class:"flex column alignCenter pop_div"},{default:c((()=>[l(C,{class:"pop_header_div"},{default:c((()=>[l(C,{class:"pop_header_text"},{default:c((()=>[u(d(e.$t("14_Top_up")),1)])),_:1})])),_:1}),l(C,{class:"pop_header_label"},{default:c((()=>[u(d(e.$t("14_remaining_power"))+" ",1),h("span",{class:"pop_header_value"},d(o.account),1)])),_:1}),l(C,{class:"flex row justifyCenter pop_item_div"},{default:c((()=>[(n(!0),p(m,null,w(o.powersList,((t,s)=>(n(),y(C,{class:P(["flex row justifyBetween alignCenter pop_item",o.powersID==t.ID?"pop_item_selected":""]),key:t.ID,onClick:e=>r.changePower(t)},{default:c((()=>[l(C,{class:"flex column justifyCenter alignCenter"},{default:c((()=>[l(C,{class:"pop_item_value"},{default:c((()=>[u(d(t.PowerAmount),1)])),_:2},1024),l(C,{class:"pop_item_label"},{default:c((()=>[u(d(e.$t("14_Computing_power")),1)])),_:1})])),_:2},1024),l(C,{class:"pop_item_money"},{default:c((()=>[u("¥"+d(t.AmountInCurrency),1)])),_:2},1024)])),_:2},1032,["class","onClick"])))),128))])),_:1}),l(v,{class:"custome_input",type:"number",placeholder:e.$t("14_Customize"),modelValue:o.powerValue,"onUpdate:modelValue":t[0]||(t[0]=e=>o.powerValue=e)},null,8,["placeholder","modelValue"]),l(C,{class:"pay_btn",onClick:t[1]||(t[1]=e=>r.handleWePay())},{default:c((()=>[u("¥"+d(o.currencySum)+" "+d(e.$t("14_Pay_now")),1)])),_:1}),l(C,{class:"flex row alignCenter agreement_div"},{default:c((()=>[l(x,{class:"btn_img",src:S}),l(C,{class:"agreement_text"},{default:c((()=>[u(d(e.$t("14_agree"))+" ",1),h("span",{class:"agreement_value"},d(e.$t("14_Agreement")),1)])),_:1})])),_:1})])),_:1})])),_:1},8,["type"]),l(k,{ref:"popupcenter",type:"center",animation:!1},{default:c((()=>[l(x,{src:o.qrCodeBase64,mode:"aspectFit"},null,8,["src"])])),_:1},512)],64)}],["__scopeId","data-v-e6d6d3c0"]]);export{j as P,S as _};