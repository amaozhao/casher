import{s as t,g as e,r as s,l as i,a as l,b as a,h as n,n as o,c,w as C,i as d,o as _,d as g,e as r,t as f,f as u,j as m,F as x,k as p,m as h}from"./index-CCXeNhnM.js";import{m as w,f as L}from"./index.DHoWcfBH.js";import{_ as v}from"./speed.Cs_aoTP_.js";import{_ as H}from"./_plugin-vue_export-helper.BCo6x5W8.js";import"./http.BGIf5Bxo.js";const b=H({data:()=>({isLogin:!0,href:"https://uniapp.dcloud.io/component/README?id=uniui",client_id:"80fd42e0-d652-4732-b209-e14edd0cc217",clientList:[]}),onLoad(e){let s=new URL(window.location.href).searchParams.get("token");s&&t("token",s),e.client_id&&(this.client_id=e.client_id)},onLoad(){this.handleLogin()},onShow:function(){},methods:{handleLogin(){if(e("token"))this.getFlowsList();else{var o=this;if("mp-weixin"===e("uniPlatform"))i({success(e){if(e.code){l({title:"加载中",mask:!0});var s=e.code;uni.getUserInfo({lang:"zh_CN",success:e=>{let i={};i.code=s,i.rawData=e.rawData,i.signature=e.signature,i.encryptedData=e.encryptedData,i.iv=e.iv,w(i).then((e=>{if(200!=e.status)return a({icon:"none",title:e.data.msg});t("token",e.data.token),a({icon:"success",title:"登录成功"}),o.handleLogin(),n()}))},fail:t=>(n(),a({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"}))})}},fail:t=>a({icon:"none",title:"亲爱的用户，您拒绝了！我就不给您跳转了。"})});else s({url:"/pages/toc/toc02Login"})}},getFlowsList(){L({client_id:this.client_id}).then((t=>{200==t.status&&(this.clientList=t.data||[])}))},goNextPage(t){this.isLogin?o({url:"/pages/toc/toc27Create?id="+t.id+"&fee="+t.fee}):s({url:"/pages/toc/toc02Login"})},goHomePage(){s({url:"/pages/toc/toc27Create"})},goRecordPage(){s({url:"/pages/toc/toc24Record"})}}},[["render",function(t,e,s,i,l,a){const n=d,o=h;return _(),c(n,{class:"flex column alignCenter bg_div"},{default:C((()=>[g(n,{class:"flex row justifyBetween alignCenter header_div"},{default:C((()=>[g(n,{class:"flex row alignCenter title_content_view",onClick:e[0]||(e[0]=t=>a.goHomePage())},{default:C((()=>[g(n,{class:"title_btn"},{default:C((()=>[r(f(t.$t("tocIndex_text1")),1)])),_:1}),g(n,{class:"title_label"},{default:C((()=>[r(f(t.$t("tocIndex_text2")),1)])),_:1})])),_:1}),g(n,{class:"title_btn2 xsHide"},{default:C((()=>[r(f(t.$t("tocIndex_text3")),1)])),_:1})])),_:1}),g(n,{class:"flex column alignCenter content_div"},{default:C((()=>[g(n,{class:"flex row wrap justifyCenter alignCenter content_item_div"},{default:C((()=>[g(o,{class:"home_image",src:l.clientList[0].images[0].image},null,8,["src"]),g(n,{class:"flex column alignCenter content_item_value"},{default:C((()=>[g(n,{class:"text1 textAlign"},{default:C((()=>[r(f(l.clientList[0].title),1)])),_:1}),g(n,{class:"text2"},{default:C((()=>[r(f(t.$t("tocIndex_text6"))+" ..",1)])),_:1}),g(n,{class:"text3"},{default:C((()=>[r(f(l.clientList[0].gn_desc),1)])),_:1}),g(n,{class:"flex row justifyCenter alignCenter btn_div",onClick:e[1]||(e[1]=t=>a.goNextPage(l.clientList[0]))},{default:C((()=>[g(o,{class:"btn_img",src:v}),g(n,{class:"btn_text"},{default:C((()=>[r(f(t.$t("start")),1)])),_:1})])),_:1}),g(n,{class:"flex row justifyBetween alignCenter options_div"},{default:C((()=>[g(n,{class:"flex column alignCenter options_item"},{default:C((()=>[g(o,{class:"options_item_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M22.3146%2016.4836L12.7484%2023.7636C12.3505%2024.0669%2011.8641%2024.2312%2011.3638%2024.2312H7.63841C6.70148%2024.2272%205.80452%2023.8512%205.14477%2023.1859C4.48502%2022.5206%204.11649%2021.6206%204.12021%2020.6836V5.85204C4.11649%204.91511%204.48502%204.01506%205.14477%203.3498C5.80452%202.68453%206.70148%202.30852%207.63841%202.30444H19.7106C20.6475%202.30852%2021.5445%202.68453%2022.2042%203.3498C22.864%204.01506%2023.2325%204.91511%2023.2288%205.85204V14.6342C23.229%2014.9921%2023.1466%2015.3451%2022.988%2015.6659C22.8295%2015.9866%2022.599%2016.2665%2022.3146%2016.4836Z'%20fill='%23019083'/%3e%3cpath%20d='M25.48%2019.0848L24.3012%2017.6288C24.173%2017.4688%2023.9869%2017.3658%2023.7832%2017.3422C23.5795%2017.3186%2023.3748%2017.3763%2023.2134%2017.5028L16.394%2022.785C16.2948%2022.8616%2016.2156%2022.9611%2016.163%2023.0748L15.3132%2024.8948C15.2506%2025.028%2015.2263%2025.1759%2015.2431%2025.3221C15.2599%2025.4683%2015.3172%2025.6068%2015.4084%2025.7222C15.4982%2025.8369%2015.6184%2025.9239%2015.7553%2025.9734C15.8922%2026.023%2016.0403%2026.0329%2016.1826%2026.0022L18.3568%2025.5486C18.4736%2025.5243%2018.5833%2025.4735%2018.6774%2025.4002L25.354%2020.209C25.4365%2020.1443%2025.5054%2020.0639%2025.5566%2019.9724C25.6078%2019.8809%2025.6404%2019.7801%2025.6524%2019.6759C25.6643%2019.5718%2025.6555%2019.4662%2025.6264%2019.3655C25.5973%2019.2648%2025.5485%2019.1708%2025.4828%2019.089L25.48%2019.0848Z'%20fill='%23A9FCF5'/%3e%3cpath%20d='M16.8238%2010.1738H10.1654C9.86837%2010.1738%209.58349%2010.0558%209.37345%209.8458C9.16341%209.63576%209.04541%209.35088%209.04541%209.05384C9.04541%208.7568%209.16341%208.47192%209.37345%208.26188C9.58349%208.05184%209.86837%207.93384%2010.1654%207.93384H16.8238C17.1209%207.93384%2017.4057%208.05184%2017.6158%208.26188C17.8258%208.47192%2017.9438%208.7568%2017.9438%209.05384C17.9438%209.35088%2017.8258%209.63576%2017.6158%209.8458C17.4057%2010.0558%2017.1209%2010.1738%2016.8238%2010.1738ZM16.8238%2015.8578H10.1654C9.86837%2015.8578%209.58349%2015.7398%209.37345%2015.5298C9.16341%2015.3198%209.04541%2015.0349%209.04541%2014.7378C9.04541%2014.4408%209.16341%2014.1559%209.37345%2013.9459C9.58349%2013.7358%209.86837%2013.6178%2010.1654%2013.6178H16.8238C17.1209%2013.6178%2017.4057%2013.7358%2017.6158%2013.9459C17.8258%2014.1559%2017.9438%2014.4408%2017.9438%2014.7378C17.9438%2015.0349%2017.8258%2015.3198%2017.6158%2015.5298C17.4057%2015.7398%2017.1209%2015.8578%2016.8238%2015.8578Z'%20fill='%23161622'/%3e%3c/svg%3e"}),g(n,{class:"options_item_text"},{default:C((()=>[r(f(t.$t("tocIndex_text4")),1)])),_:1})])),_:1}),g(n,{class:"flex column alignCenter options_item",onClick:e[2]||(e[2]=t=>a.goRecordPage())},{default:C((()=>[g(o,{class:"options_item_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.5%2022.1667V5.83337C3.5%204.90512%203.86875%204.01488%204.52513%203.3585C5.1815%202.70212%206.07174%202.33337%207%202.33337H16.4523C16.7818%202.3333%2017.1076%202.40303%2017.4083%202.53796C17.7089%202.67289%2017.9775%202.86996%2018.1965%203.11621L21.5775%206.91954C21.9577%207.34737%2022.1674%207.90002%2022.1667%208.47237V12.0062C21.4093%2011.7812%2020.6234%2011.6672%2019.8333%2011.6679C18.1644%2011.6653%2016.535%2012.1765%2015.1667%2013.132V12.8334H8.16667V15.1667H13.1308C12.1753%2016.5351%2011.6641%2018.1644%2011.6667%2019.8334C11.6667%2022.1189%2012.6058%2024.185%2014.1178%2025.6667H7C6.07174%2025.6667%205.1815%2025.298%204.52513%2024.6416C3.86875%2023.9852%203.5%2023.095%203.5%2022.1667ZM8.16667%2010.5H16.3333V8.16671H8.16667V10.5Z'%20fill='%23019083'/%3e%3cpath%20d='M19.8333%2014C21.31%2014.173%2022.6649%2014.9032%2023.6213%2016.0414C24.5778%2017.1797%2025.0636%2018.6401%2024.9797%2020.1245C24.8957%2021.6088%2024.2482%2023.0051%2023.1694%2024.0282C22.0907%2025.0513%2020.6621%2025.624%2019.1753%2025.6293C17.695%2025.461%2016.3351%2024.7327%2015.3747%2023.5937C14.4143%2022.4547%2013.9261%2020.9913%2014.0102%2019.5038C14.0944%2018.0163%2014.7446%2016.6174%2015.8273%2015.594C16.9101%2014.5705%2018.3435%2014.0002%2019.8333%2014ZM18.9583%2019.5417H23.3333V17.7917H20.7083V15.1667H18.9583V19.5417Z'%20fill='%23A9FCF5'/%3e%3c/svg%3e"}),g(n,{class:"options_item_text"},{default:C((()=>[r(f(t.$t("tocIndex_text3")),1)])),_:1})])),_:1}),g(n,{class:"flex column alignCenter options_item"},{default:C((()=>[g(o,{class:"options_item_img",src:"data:image/svg+xml,%3csvg%20width='28'%20height='28'%20viewBox='0%200%2028%2028'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M13.9727%201.75C7.20508%201.75%201.72266%207.23242%201.72266%2014C1.72266%2020.7648%207.20781%2026.25%2013.9727%2026.25C20.7375%2026.25%2026.2227%2020.7648%2026.2227%2014C26.2227%207.23242%2020.7375%201.75%2013.9727%201.75ZM12.1461%2014C12.1461%2014.2789%2012.0887%2014.5469%2011.9875%2014.7902L15.3562%2017.0352C15.6844%2016.8027%2016.0863%2016.666%2016.5184%2016.666C17.6367%2016.666%2018.5445%2017.5738%2018.5445%2018.6922C18.5445%2019.8105%2017.6367%2020.7184%2016.5184%2020.7184C15.4%2020.7184%2014.4922%2019.8105%2014.4922%2018.6922C14.4922%2018.5363%2014.5113%2018.3859%2014.5441%2018.2383L10.9512%2015.843C10.6969%2015.9578%2010.4152%2016.0234%2010.1172%2016.0234C8.99883%2016.0234%208.09102%2015.1156%208.09102%2013.9973C8.09102%2012.8789%208.99883%2011.9711%2010.1172%2011.9711C10.4152%2011.9711%2010.6969%2012.0367%2010.9512%2012.1516L14.5441%209.75625C14.5113%209.61133%2014.4922%209.4582%2014.4922%209.30234C14.4922%208.18398%2015.4%207.27617%2016.5184%207.27617C17.6367%207.27617%2018.5445%208.18398%2018.5445%209.30234C18.5445%2010.4207%2017.6367%2011.3285%2016.5184%2011.3285C16.0863%2011.3285%2015.6844%2011.1918%2015.3562%2010.9594L11.9875%2013.2043C12.0887%2013.4531%2012.1461%2013.7184%2012.1461%2014Z'%20fill='%23019083'/%3e%3c/svg%3e"}),g(n,{class:"options_item_text"},{default:C((()=>[r(f(t.$t("tocIndex_text5")),1)])),_:1})])),_:1})])),_:1})])),_:1}),l.clientList.length>1?(_(),c(n,{key:0,class:"flex row wrap justifyCenter alignCenter bottom_div"},{default:C((()=>[(_(!0),u(x,null,m(l.clientList,((t,e)=>(_(),c(n,{class:"flex row bottom_item",key:t.id,onClick:e=>a.goNextPage(t)},{default:C((()=>[0!==e?(_(),u(x,{key:0},[g(o,{class:"bottom_item_img",src:t.images[0].image},null,8,["src"]),g(n,{class:"flex column justifyCenter"},{default:C((()=>[g(n,{class:"bottom_item_label"},{default:C((()=>[r(f(t.title),1)])),_:2},1024),g(n,{class:"bottom_item_value"},{default:C((()=>[r(f(t.gn_desc),1)])),_:2},1024)])),_:2},1024)],64)):p("",!0)])),_:2},1032,["onClick"])))),128))])),_:1})):p("",!0)])),_:1})])),_:1})])),_:1})}],["__scopeId","data-v-1c9e8416"]]);export{b as default};
