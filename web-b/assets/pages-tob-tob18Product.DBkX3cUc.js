import{b as t,d as e,n as l,r as a,H as s,e as i,f as c,w as n,i as o,o as d,j as r,k as _,m as u,t as f,u as p,p as C,q as h,F as g,v as m,x as w,y as x}from"./index-DdxUVI9G.js";import{_ as b,a as v}from"./uni-row.DNqPMETx.js";import{C as k,f as y,h as H,c as L,a as j,i as V,j as M,k as B,r as P}from"./index.6Zyrx_vJ.js";import{f as $,b as Z,a as S,c as T,_ as D}from"./githup.Dv-BGyaE.js";import{P as I}from"./index.Czp7_VS2.js";import{_ as F}from"./home.DYYpJuyZ.js";import{_ as G,a as A}from"./speed.FiO8-Deg.js";import{_ as E}from"./_plugin-vue_export-helper.BCo6x5W8.js";import"./browser.CKbbJXUY.js";const R=E({components:{Pay:I,Content:k},data:()=>({appStatusBarHeight:0,href:"https://uniapp.dcloud.io/component/README?id=uniui",templatelist:[],cappList:[],productList:[],timer:null}),onShow:function(){this.getCappsList(),this.clearTimer(),this.timer=setInterval((()=>{this.getCappsList()}),2e3),this.getflowsList(),this.getb_templates();let{statusBarHeight:e}=t();e>0&&(this.appStatusBarHeight=40+e)},methods:{handlebqrcode(t){y({workflow_id:t}).then((t=>{t.status}))},handleTo(){let t=this.cappList.find((t=>"Status"==t.Status));t?this.openHref(t.Path):this.goProductPage()},handlebanner(){H().then((t=>{200==t.status&&e({icon:"success",title:"去除成功"})}))},handlecomfyui(){L().then((t=>{200==t.status&&this.openHref(t.url)}))},getflowsList(){$().then((t=>{200==t.status&&(this.productList=t.data)}))},getb_templates(){Z().then((t=>{200==t.status&&(this.templatelist=t.data||[])}))},goCpuProduct(){l({url:"/pages/tob/tob18Product"})},getCappsList(){j().then((t=>{2e4==t.code&&(this.cappList=t.data.containers||[])}))},goProductPage(){l({url:"/pages/tob/tob17Create"})},onHomeTab(){a({url:"/pages/index/index"})},onMeTab(){a({url:"/pages/tob/tob15Me"})},handleStartCapp(t){V(t).then((t=>{2e4==t.code&&(this.getCappsList(),e({icon:"success",title:"启动成功"}))}))},handleStopCapp(t){switch(t.Status){case"running":M(t.ID).then((t=>{2e4==t.code&&(this.getCappsList(),e({icon:"success",title:"操作成功"}))}));break;case"stopped":this.handleStartCapp(t.ID)}},handleDelCapp(t){B(t).then((t=>{2e4==t.code&&(this.getCappsList(),e({icon:"success",title:"释放成功"}))}))},openHref(t,e){e||window.open(t)},openCom(t,e){"running"==e&&window.open(t)},clearTimer(){this.timer&&(clearInterval(this.timer),this.timer=null)},handlePut(t){S(t).then((t=>{200==t.status&&(e({icon:"success",title:"下架成功"}),this.getflowsList())}))},handleDel(t){T(t).then((t=>{200==t.status&&(e({icon:"success",title:"删除成功"}),this.getflowsList())}))}},beforeUnmount(){this.clearTimer()}},[["render",function(t,e,l,a,k,y){const H=s("Content"),L=m,j=o,V=P(i("uni-col"),b),M=P(i("uni-row"),v);return d(),c(j,{class:"flex column alignCenter bg_div"},{default:n((()=>[r(H),r(j,{class:"flex row justifyBetween alignCenter header_div",style:u("margin-top:"+k.appStatusBarHeight+"rpx")},{default:n((()=>[r(j,{class:"flex row alignCenter",onClick:e[0]||(e[0]=t=>y.onHomeTab())},{default:n((()=>[r(L,{class:"header_img",src:F}),r(j,{class:"title"},{default:n((()=>[_("Deploy AI")])),_:1})])),_:1}),r(j,{class:"flex row justifyCenter alignCenter tab_div"},{default:n((()=>[r(j,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:e[1]||(e[1]=t=>y.goCpuProduct())},{default:n((()=>[r(L,{class:"tab_img",src:F}),r(j,{class:"tab_label"},{default:n((()=>[_("complaint")])),_:1})])),_:1}),r(j,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:e[2]||(e[2]=t=>y.onMeTab())},{default:n((()=>[r(L,{class:"tab_img",src:G}),r(j,{class:"tab_label"},{default:n((()=>[_("me")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),r(j,{class:"flex column alignCenter div_content"},{default:n((()=>[k.cappList.length?(d(),c(j,{key:0,class:"flex row tab_item_div"},{default:n((()=>[r(j,{class:"flex detail_item justifyCenter"},{default:n((()=>[r(j,{class:"skewDiv text1"},{default:n((()=>[r(j,{class:"skew"}),r(j,{class:"skewTitle"},{default:n((()=>[_(f(t.$t("product_text1")),1)])),_:1})])),_:1})])),_:1})])),_:1})):p("",!0),(d(!0),C(g,null,h(k.cappList,((e,l)=>(d(),c(j,{class:"flex row wrap card1",key:e.ID},{default:n((()=>[r(j,{class:"flex column justifyStart card1_item"},{default:n((()=>[r(j,{class:"card1_item_title"},{default:n((()=>[_(f(e.Name)+" ",1),w("span",{class:"red subTitle"},"（"+f(e.SubTitle)+"）",1)])),_:2},1024),r(j,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:n((()=>[r(j,{class:"card1_item_value"},{default:n((()=>[_(f(e.GpuType),1)])),_:2},1024),r(j,{class:"flex column"},{default:n((()=>[r(j,{class:"card1_item_value2"},{default:n((()=>[w("span",{class:"color_green"},f(e.VramGB)+"G",1),_(" "+f(t.$t("product_text6")),1)])),_:2},1024),r(j,{class:"card1_item_value2"},{default:n((()=>[w("span",{class:"color_green"},f(e.MemoryGB)+"G",1),_(" "+f(t.$t("product_text7")),1)])),_:2},1024)])),_:2},1024)])),_:2},1024),r(j,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:n((()=>[r(j,{class:"card1_item_value2"},{default:n((()=>[_(f(t.$t("product_text8")),1)])),_:1}),r(j,{class:"card1_item_value2"},{default:n((()=>[_(f(e.EndTime),1)])),_:2},1024)])),_:2},1024)])),_:2},1024),r(j,{class:"flex column justifyBetween alignCenter card1_item"},{default:n((()=>[r(j,{class:x(["card1_item_btn","running"!==e.Status?"disabled":""]),onClick:t=>y.openCom(e.Path,e.Status)},{default:n((()=>[_(f(t.$t("product_text12")),1)])),_:2},1032,["class","onClick"]),r(j,{class:"flex row option_btn_div"},{default:n((()=>[r(j,{class:"flex column alignCenter option_item",onClick:t=>y.openHref(e.FileManager)},{default:n((()=>[r(L,{class:"option_img",src:"data:image/svg+xml,%3csvg%20width='21'%20height='20'%20viewBox='0%200%2021%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M2.375%2020V0H11.125V7.5H18.625V20H2.375ZM11.75%2012.5H9.875V9.375H4.875V17.5H11.75V12.5ZM6.75%2014.375H9.875V16.25H6.75V14.375ZM6.75%2011.25H8.625V13.125H6.75V11.25Z'%20fill='%23FF9E1F'/%3e%3cpath%20d='M12.375%200L18.625%206.25H12.375V0Z'%20fill='%23FFD7A4'/%3e%3c/svg%3e"}),r(j,{class:"option_label"},{default:n((()=>[_(f(t.$t("product_text9")),1)])),_:1})])),_:2},1032,["onClick"]),r(j,{class:"flex column alignCenter option_item",onClick:t=>y.handleStopCapp(e)},{default:n((()=>[r(L,{class:"option_img",src:"data:image/svg+xml,%3csvg%20width='20'%20height='20'%20viewBox='0%200%2020%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M10%201.25C5.17188%201.25%201.25%205.17188%201.25%2010C1.25%2014.8281%205.17188%2018.75%2010%2018.75C14.8281%2018.75%2018.75%2014.8281%2018.75%2010C18.75%205.17188%2014.8281%201.25%2010%201.25ZM9.375%203.75H10.625V11.25H9.375V3.75ZM10%2016.25C6.54688%2016.25%203.75%2013.4531%203.75%2010C3.75%207.4375%205.29688%205.23437%207.5%204.26562V5.67188C6%206.53125%205%208.15625%205%2010C5%2012.75%207.25%2015%2010%2015C12.75%2015%2015%2012.75%2015%2010C15%208.15625%2014%206.53125%2012.5%205.67188V4.26562C14.7031%205.23437%2016.25%207.4375%2016.25%2010C16.25%2013.4531%2013.4531%2016.25%2010%2016.25Z'%20fill='black'/%3e%3c/svg%3e"}),"running"==e.Status?(d(),c(j,{key:0,class:"option_label"},{default:n((()=>[_(f(t.$t("product_Close")),1)])),_:1})):"stopped"==e.Status?(d(),c(j,{key:1,class:"option_label"},{default:n((()=>[_(f(t.$t("product_Run")),1)])),_:1})):(d(),c(j,{key:2,class:"option_label"},{default:n((()=>[_(f(e.Label),1)])),_:2},1024))])),_:2},1032,["onClick"]),"stopped"==e.Status?(d(),c(j,{key:0,class:"flex column alignCenter option_item",onClick:t=>y.handleDelCapp(e.ID)},{default:n((()=>[r(L,{class:"option_img",src:"data:image/svg+xml,%3csvg%20width='20'%20height='20'%20viewBox='0%200%2020%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_18_738)'%3e%3cpath%20d='M14.8267%200.850098H5.17338C2.78558%200.850098%200.849976%202.7857%200.849976%205.1735V14.8268C0.849976%2017.2145%202.78558%2019.1501%205.17338%2019.1501H14.8267C17.2144%2019.1501%2019.15%2017.2145%2019.15%2014.8268V5.1735C19.15%202.7857%2017.2144%200.850098%2014.8267%200.850098ZM4.40688%204.4167C5.49788%203.1893%207.27088%203.1893%208.36188%204.4167L10.544%206.5988L9.45298%207.5535L7.27088%205.5078C6.72528%204.9623%205.90708%204.9623%205.49788%205.5078C5.08878%206.0533%204.95238%206.8716%205.49788%207.2808L7.67998%209.4628L6.45258%2010.5538L4.40688%208.3718C3.17948%207.2808%203.17948%205.5078%204.40688%204.4167ZM4.40688%2015.7363C4.13408%2015.4636%204.13408%2014.918%204.40688%2014.509L14.6354%204.2803C14.9083%204.0075%2015.4538%204.0075%2015.8629%204.2803C16.1357%204.5531%2016.1357%205.0986%2015.8629%205.5077L5.63438%2015.7363C5.22518%2016.1455%204.67968%2016.1455%204.40688%2015.7363ZM15.5901%2015.6C14.4991%2016.691%2012.7262%2016.691%2011.6351%2015.6L9.45298%2013.4179L10.544%2012.3269L12.7262%2014.509C13.2717%2015.0545%2014.0899%2015.0545%2014.4991%2014.509C15.0446%2013.9634%2015.0446%2013.1451%2014.4991%2012.736L12.4534%2010.5539L13.5444%209.4629L15.7266%2011.645C16.8177%2012.7359%2016.8177%2014.509%2015.5901%2015.6Z'%20fill='black'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_18_738'%3e%3crect%20width='20'%20height='20'%20fill='white'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"}),r(j,{class:"option_label"},{default:n((()=>[_(f(t.$t("product_text10")),1)])),_:1})])),_:2},1032,["onClick"])):p("",!0)])),_:2},1024)])),_:2},1024)])),_:2},1024)))),128)),r(j,{class:"flex row tab_item_div"},{default:n((()=>[r(j,{class:"flex detail_item justifyCenter"},{default:n((()=>[r(j,{class:"skewDiv text1"},{default:n((()=>[r(j,{class:"skew"}),r(j,{class:"skewTitle"},{default:n((()=>[_(f(t.$t("18_My_work")),1)])),_:1})])),_:1})])),_:1})])),_:1}),r(j,{class:"flex row justifyCenter alignCenter wrap btn_view"},{default:n((()=>[r(M,{style:{width:"100%"}},{default:n((()=>[r(V,{xs:24,sm:24,md:11,lg:12,xl:12},{default:n((()=>[r(j,{class:"btn1 flex alignCenter justifyCenter",onClick:e[3]||(e[3]=t=>y.handlecomfyui())},{default:n((()=>[r(L,{class:"githupcss",src:D}),_(" "+f(t.$t("18_ComfyUI_generation")),1)])),_:1})])),_:1}),r(V,{xs:0,sm:0,md:2,lg:2,xl:2},{default:n((()=>[_("1")])),_:1}),r(V,{xs:24,sm:24,md:{span:11,push:2},lg:{span:11,push:1},xl:{span:11,push:2}},{default:n((()=>[r(j,{class:"btn2 relative",onClick:e[4]||(e[4]=t=>y.handleTo())},{default:n((()=>[_(f(t.$t("18_Online_generation"))+" ",1),r(j,{class:"btn2Text"},{default:n((()=>[_(f(t.$t("product_text5")),1)])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),(d(!0),C(g,null,h(k.productList,(e=>(d(),c(j,{class:"flex row wrap btn_view",key:e.id},{default:n((()=>[r(j,{class:"flex row justifyBetween alignCenter card2_item"},{default:n((()=>[r(L,{class:"product_img",mode:"aspectFill",src:e.images[0].image},null,8,["src"]),r(j,{class:"flex column product_value_item"},{default:n((()=>[r(j,{class:"product_value_label"},{default:n((()=>[_(f(e.gn_desc),1)])),_:2},1024),r(j,{class:"flex row justifyBetween product_value"},{default:n((()=>[r(j,null,{default:n((()=>[_(f(t.$t("tobProduct_text1")),1)])),_:1}),r(j,null,{default:n((()=>[_(f(e.created),1)])),_:2},1024)])),_:2},1024),r(j,{class:"flex row justifyBetween product_value"},{default:n((()=>[r(j,null,{default:n((()=>[_(f(t.$t("tobProduct_text2")),1)])),_:1}),r(j,null,{default:n((()=>[_(f(e.view_count),1)])),_:2},1024)])),_:2},1024),r(j,{class:"flex row justifyBetween product_value"},{default:n((()=>[r(j,null,{default:n((()=>[_(f(t.$t("tobProduct_text3")),1)])),_:1}),r(j,null,{default:n((()=>[_(f(e.task_count),1)])),_:2},1024)])),_:2},1024)])),_:2},1024)])),_:2},1024),r(j,{class:"flex row justifyBetween wrap card2_item2"},{default:n((()=>[r(j,{class:"flex row justifyBetween card2_right_item"},{default:n((()=>[r(j,{class:"card2_right_label"},{default:n((()=>[w("span",{class:"card2_right_head"},f(t.$t("tobIndex_text8"))+"URL:",1),_(" "+f(e.preview_url),1)])),_:2},1024),r(j,{class:"card2_right_copy",onClick:t=>y.openHref(e.preview_url)},{default:n((()=>[_(f(t.$t("tobIndex_text9")),1)])),_:2},1032,["onClick"])])),_:2},1024),r(j,{class:"flex row justifyBetween card2_right_item"},{default:n((()=>[r(j,{class:"flex column alignCenter option_item",onClick:t=>y.handlebqrcode(e.id)},{default:n((()=>[r(L,{class:"option_img",src:"data:image/svg+xml,%3csvg%20width='21'%20height='20'%20viewBox='0%200%2021%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_18_832)'%3e%3cpath%20d='M10.5%200C8.52219%200%206.58879%200.58649%204.9443%201.6853C3.29981%202.78412%202.01809%204.3459%201.26121%206.17317C0.504333%208.00043%200.306299%2010.0111%200.692152%2011.9509C1.078%2013.8907%202.03041%2015.6725%203.42894%2017.0711C4.82746%2018.4696%206.60929%2019.422%208.5491%2019.8079C10.4889%2020.1937%2012.4996%2019.9957%2014.3268%2019.2388C16.1541%2018.4819%2017.7159%2017.2002%2018.8147%2015.5557C19.9135%2013.9112%2020.5%2011.9778%2020.5%2010C20.5%207.34784%2019.4464%204.8043%2017.5711%202.92893C15.6957%201.05357%2013.1522%200%2010.5%200ZM15.514%208.98801C15.1243%209.61282%2014.5163%2010.0704%2013.808%2010.272C13.6536%2010.3224%2013.4924%2010.3494%2013.33%2010.352C13.1799%2010.3511%2013.0363%2010.2909%2012.9305%2010.1845C12.8247%2010.078%2012.7653%209.93406%2012.7653%209.78399C12.7653%209.63393%2012.8247%209.48996%2012.9305%209.38353C13.0363%209.27711%2013.1799%209.21688%2013.33%209.216C13.3732%209.21699%2013.4162%209.20881%2013.456%209.19199C13.9109%209.07894%2014.3031%208.79162%2014.548%208.39199C14.6905%208.15907%2014.7653%207.89106%2014.764%207.61801C14.764%206.72%2013.934%205.98%2012.922%205.98C12.5718%205.98074%2012.2276%206.07092%2011.922%206.24199C11.6701%206.37464%2011.4582%206.57209%2011.3081%206.81397C11.1579%207.05586%2011.0751%207.33341%2011.068%207.61801V12.388C11.063%2012.8712%2010.9287%2013.3442%2010.679%2013.7578C10.4293%2014.1714%2010.0733%2014.5106%209.64801%2014.74C9.1726%2015.0073%208.63539%2015.1452%208.09%2015.14C6.442%2015.14%205.09%2013.9%205.09%2012.366C5.09292%2011.8848%205.22632%2011.4134%205.476%2011.002C5.86569%2010.3772%206.47374%209.91955%207.182%209.71801C7.33662%209.66835%207.49764%209.6414%207.66001%209.63801C7.73488%209.63757%207.80909%209.65194%207.87839%209.68028C7.94769%209.70863%208.0107%209.7504%208.0638%209.80319C8.1169%209.85598%208.15903%209.91874%208.18779%209.98787C8.21654%2010.057%208.23134%2010.1311%208.23134%2010.206C8.23134%2010.2809%208.21654%2010.355%208.18779%2010.4241C8.15903%2010.4933%208.1169%2010.556%208.0638%2010.6088C8.0107%2010.6616%207.94769%2010.7034%207.87839%2010.7317C7.80909%2010.7601%207.73488%2010.7744%207.66001%2010.774C7.61678%2010.773%207.57384%2010.7812%207.53401%2010.798C7.08305%2010.9193%206.69362%2011.2046%206.44202%2011.598C6.29952%2011.8309%206.22472%2012.0989%206.226%2012.372C6.226%2013.27%207.056%2014.01%208.08%2014.01C8.43021%2014.0093%208.77442%2013.9191%209.08%2013.748C9.33152%2013.6151%209.54305%2013.4175%209.69281%2013.1757C9.84257%2012.9338%209.92513%2012.6564%209.932%2012.372V7.62402C9.93743%207.14046%2010.0722%206.66716%2010.3222%206.25324C10.5723%205.83931%2010.9285%205.49983%2011.354%205.27002C11.8208%204.99029%2012.3558%204.84494%2012.9%204.85002C14.548%204.85002%2015.9%206.09002%2015.9%207.62402C15.8971%208.10524%2015.7637%208.57664%2015.514%208.98803V8.98801Z'%20fill='%2300B240'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_18_832'%3e%3crect%20width='20'%20height='20'%20fill='white'%20transform='translate(0.5)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"}),r(j,{class:"option_label"},{default:n((()=>[_(f(t.$t("tobProduct_text4")),1)])),_:1})])),_:2},1032,["onClick"]),r(j,{class:"flex column alignCenter option_item",onClick:t=>y.handlePut(e.id)},{default:n((()=>[r(L,{class:"option_img",src:"data:image/svg+xml,%3csvg%20width='21'%20height='20'%20viewBox='0%200%2021%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_18_830)'%3e%3cpath%20d='M19.8262%203.46852H1.06058C0.652433%203.46852%200.431976%203.01475%200.694141%202.71696L2.95829%200.161656C3.05065%200.0595575%203.18471%200%203.32473%200H16.9901C17.1122%200%2017.2314%200.045377%2017.3208%200.124787L20.1569%202.68009C20.4697%202.9637%2020.2582%203.46852%2019.8262%203.46852ZM20.5204%205.46795H0.479642C0.214498%205.46795%200%205.67215%200%205.92456V19.5434C0%2019.7958%200.214498%2020%200.479642%2020H20.5204C20.7855%2020%2021%2019.7958%2021%2019.5434V5.92456C21%205.67215%2020.7855%205.46795%2020.5204%205.46795ZM13.7786%2013.7124L10.7845%2016.5598C10.5968%2016.7385%2010.29%2016.7385%2010.1023%2016.5598L7.11122%2013.7124C6.80735%2013.4231%207.02185%2012.9297%207.45084%2012.9297H9.39325V9.42144C9.39325%209.16903%209.60775%208.962%209.87587%208.962H11.0139C11.279%208.962%2011.4965%209.16619%2011.4965%209.42144V12.9297H13.4389C13.8649%2012.9297%2014.0824%2013.4231%2013.7786%2013.7124Z'%20fill='%23D1AB21'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_18_830'%3e%3crect%20width='20'%20height='20'%20fill='white'%20transform='translate(0.5)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"}),r(j,{class:"option_label"},{default:n((()=>[_(f(t.$t("tobProduct_text5")),1)])),_:1})])),_:2},1032,["onClick"]),r(j,{class:"flex column alignCenter option_item",onClick:t=>y.handleDel(e.id)},{default:n((()=>[r(L,{class:"option_img",src:"data:image/svg+xml,%3csvg%20width='24'%20height='24'%20viewBox='0%200%2024%2024'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M17.9865%205.00014H14.9291C14.9291%204.42453%2014.4812%203.729%2013.9283%203.729H10.4267C9.87379%203.729%209.42594%204.42453%209.42594%205.00014H6.36862C5.69386%205.00014%204.9502%205.10095%204.9502%205.777V6.82291H19.0526V5.777C19.0527%205.10097%2018.6623%205.00014%2017.9865%205.00014Z'%20fill='white'/%3e%3cpath%20d='M6.19727%208.0459V18.006C6.19727%2019.0188%207.19022%2020.2536%208.20293%2020.2536H16.1519C17.1658%2020.2536%2017.8294%2019.0188%2017.8294%2018.006V8.0459H6.19727ZM9.53734%2018.2143H8.31361V9.40074H9.53734V18.2143ZM12.6026%2018.2143H11.3789V9.40074H12.6026V18.2143ZM15.6679%2018.2143H14.4441V9.40074H15.6679V18.2143Z'%20fill='white'/%3e%3c/svg%3e"}),r(j,{class:"option_label"},{default:n((()=>[_(f(t.$t("tobProduct_text6")),1)])),_:1})])),_:2},1032,["onClick"])])),_:2},1024),r(j,{class:"flex row justifyBetween card2_right_item"},{default:n((()=>[r(j,{class:"card2_right_btn",onClick:t=>y.handlebanner(e.id)},{default:n((()=>[_(f(t.$t("tobProduct_text7")),1)])),_:2},1032,["onClick"]),r(j,{class:"card2_right_btn"},{default:n((()=>[_(f(t.$t("tobProduct_text8")),1)])),_:1})])),_:2},1024)])),_:2},1024)])),_:2},1024)))),128)),r(j,{class:"flex row tab_item_div"},{default:n((()=>[r(j,{class:"flex detail_item justifyCenter"},{default:n((()=>[r(j,{class:"skewDiv text1"},{default:n((()=>[r(j,{class:"skew"}),r(j,{class:"skewTitle"},{default:n((()=>[_(f(t.$t("18_Stencil")),1)])),_:1})])),_:1})])),_:1})])),_:1}),(d(!0),C(g,null,h(k.templatelist,((l,a)=>(d(),c(j,{class:"flex row wrap btn_view",key:l.id},{default:n((()=>[r(j,{class:"flex row alignCenter card2_item",style:{height:"90px"}},{default:n((()=>[r(L,{class:"product_img",mode:"aspectFill",src:l.images[0].image,style:{height:"90px",width:"90px"}},null,8,["src"]),r(j,{class:"flex column justifyStart alignStart product_value_item"},{default:n((()=>[r(j,{class:"product_value_label"},{default:n((()=>[_(f(l.title)+"2",1)])),_:2},1024)])),_:2},1024)])),_:2},1024),r(j,{class:"flex row justifyBetween wrap card2_item2",style:{height:"90px"}},{default:n((()=>[r(j,{class:"flex row justifyBetween card2_right_item"},{default:n((()=>[r(j,{class:"card2_right_label"},{default:n((()=>[w("span",{class:"card2_right_head"},f(t.$t("tobIndex_text8"))+"URL:",1),_(" "+f(l.preview_url),1)])),_:2},1024),r(j,{class:"card2_right_copy",onClick:t=>y.openHref(l.preview_url)},{default:n((()=>[_(f(t.$t("tobIndex_text9")),1)])),_:2},1032,["onClick"])])),_:2},1024),r(j,{class:"flex row justifyCenter card2_right_item"},{default:n((()=>[r(j,{class:"flex row justifyCenter alignCenter btn_div",onClick:e[5]||(e[5]=e=>t.goCreatePage())},{default:n((()=>[r(L,{class:"btn_img",src:A}),r(j,{class:"btn_text"},{default:n((()=>[_(f(t.$t("tobIndex_text7")),1)])),_:1})])),_:1})])),_:1})])),_:2},1024)])),_:2},1024)))),128))])),_:1})])),_:1})}],["__scopeId","data-v-b8b5f8f7"]]);export{R as default};
