import{e,f as a,h as l,b as t,w as s,j as i,o as n,k as c,d as r,a as o,t as u,c as d,v as f,F as _,p as A,q as p}from"./index-C4OrJxFS.js";import{r as m,c as g,_ as x,a as C}from"./http.CJFcfz4y.js";import{r as w}from"./uni-app.es.C71S0I2S.js";import{_ as b,a as h}from"./home.CDDtgVUx.js";import{_ as k,a as y,b as j}from"./speed.BCEs_Q6L.js";import{_ as B,a as v,b as R}from"./connect.CJQmslJ0.js";const J=b({data:()=>({appStatusBarHeight:0,href:"https://uniapp.dcloud.io/component/README?id=uniui",cappList:[]}),onShow:function(){this.getCappsList();let{statusBarHeight:a}=e();a>0&&(this.appStatusBarHeight=40+a)},methods:{getCappsList(){var e;m.httpRequest({url:g.cappsList,method:"GET"},e).then((e=>{2e4==e.code&&(this.cappList=e.data.containers||[])}))},goCreatePage(){a({url:"/pages/web/web14GpuCreate"})},onLeftTab(){a({url:"/pages/index/index"})},onHomeTab(){a({url:"/pages/web/web14GpuCreate"})},onMeTab(){a({url:"/pages/tob/tob15Me"})}}},[["render",function(e,a,m,g,b,J){const D=p,I=i,U=w(l("uni-col"),x),F=w(l("uni-row"),C);return n(),t(I,{class:"flex column alignCenter bg_div"},{default:s((()=>[c(I,{class:"flex row justifyBetween alignCenter header_div",style:o("margin-top:"+b.appStatusBarHeight+"rpx")},{default:s((()=>[c(I,{class:"flex row alignCenter",onClick:a[0]||(a[0]=e=>J.onLeftTab())},{default:s((()=>[c(D,{class:"header_img",src:h}),c(I,{class:"title"},{default:s((()=>[r("Deploy AI")])),_:1})])),_:1}),c(I,{class:"flex row justifyCenter alignCenter tab_div"},{default:s((()=>[c(I,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[1]||(a[1]=e=>J.onHomeTab())},{default:s((()=>[c(D,{class:"tab_img",src:h}),c(I,{class:"tab_label"},{default:s((()=>[r("complaint")])),_:1})])),_:1}),c(I,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[2]||(a[2]=e=>J.onMeTab())},{default:s((()=>[c(D,{class:"tab_img",src:k}),c(I,{class:"tab_label"},{default:s((()=>[r("me")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),c(I,{class:"flex column alignCenter div_content"},{default:s((()=>[c(I,{class:"skewDiv text1"},{default:s((()=>[c(I,{class:"skew"}),c(I,{class:"skewTitle"},{default:s((()=>[r(u(e.$t("18_My_example")),1)])),_:1})])),_:1}),(n(!0),d(_,null,f(b.cappList,((a,l)=>(n(),t(I,{class:"flex row wrap card1 pd20",key:a.ID},{default:s((()=>[c(I,{class:"flex column justifyStart card1_item"},{default:s((()=>[c(I,{class:"card1_item_title"},{default:s((()=>[r(u(a.Name)+" ",1),A("span",{class:"red subTitle"},"（"+u(a.SubTitle)+"）",1)])),_:2},1024),c(I,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:s((()=>[c(I,{class:"card1_item_value"},{default:s((()=>[r(u(a.GpuType),1)])),_:2},1024),c(I,{class:"flex column"},{default:s((()=>[c(I,{class:"card1_item_value2"},{default:s((()=>[A("span",{class:"color_green"},u(a.VramGB)+"G",1),r(" 显存 ")])),_:2},1024),c(I,{class:"card1_item_value2"},{default:s((()=>[A("span",{class:"color_green"},u(a.MemoryGB)+"G",1),r(" 空间 ")])),_:2},1024)])),_:2},1024)])),_:2},1024),c(I,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:s((()=>[c(I,{class:"card1_item_value2"},{default:s((()=>[r("到期时间")])),_:1}),c(I,{class:"card1_item_value2"},{default:s((()=>[r(u(a.EndTime),1)])),_:2},1024)])),_:2},1024)])),_:2},1024),c(I,{class:"flex column justifyBetween alignCenter card1_item"},{default:s((()=>[c(I,{class:"card1_item_btn",onClick:l=>e.handleStartCapp(a.ID)},{default:s((()=>[r("打开comfyUI")])),_:2},1032,["onClick"]),c(I,{class:"flex row option_btn_div"},{default:s((()=>[c(I,{class:"flex column alignCenter option_item",onClick:l=>e.openHref(a.FileManager)},{default:s((()=>[c(D,{class:"option_img",src:B}),c(I,{class:"option_label"},{default:s((()=>[r("文件管理")])),_:1})])),_:2},1032,["onClick"]),c(I,{class:"flex column alignCenter option_item",onClick:l=>e.handleStopCapp(a.ID)},{default:s((()=>[c(D,{class:"option_img",src:v}),c(I,{class:"option_label"},{default:s((()=>[r("关机")])),_:1})])),_:2},1032,["onClick"]),c(I,{class:"flex column alignCenter option_item",onClick:l=>e.handleDelCapp(a.ID)},{default:s((()=>[c(D,{class:"option_img",src:R}),c(I,{class:"option_label"},{default:s((()=>[r("释放")])),_:1})])),_:2},1032,["onClick"])])),_:2},1024)])),_:2},1024)])),_:2},1024)))),128)),c(I,{class:"flex detail_item justifyCenter"},{default:s((()=>[c(I,{class:"skewDiv text2"},{default:s((()=>[c(I,{class:"skew"}),c(I,{class:"skewTitle"},{default:s((()=>[r(u(e.$t("18_My_work")),1)])),_:1})])),_:1})])),_:1}),c(I,{class:"flex row justifyCenter alignCenter wrap btn_view"},{default:s((()=>[c(F,{style:{width:"100%"}},{default:s((()=>[c(U,{xs:24,sm:24,md:11,lg:12,xl:12},{default:s((()=>[c(I,{class:"btn1",onClick:a[3]||(a[3]=a=>e.goProductPage())},{default:s((()=>[r(u(e.$t("18_ComfyUI_generation")),1)])),_:1})])),_:1}),c(U,{xs:0,sm:0,md:2,lg:2,xl:2},{default:s((()=>[r("1")])),_:1}),c(U,{xs:24,sm:24,md:{span:11,push:2},lg:{span:11,push:1},xl:{span:11,push:2}},{default:s((()=>[c(I,{class:"btn2 relative"},{default:s((()=>[r(u(e.$t("18_Online_generation")),1)])),_:1})])),_:1})])),_:1})])),_:1}),(n(!0),d(_,null,f(b.cappList,((a,l)=>(n(),t(I,{class:"flex row wrap card1",key:a.ID},{default:s((()=>[c(U,{xs:24,sm:12,md:12,lg:12,xl:12},{default:s((()=>[c(I,{class:"flex justifyStart alignCenter leftDiv"},{default:s((()=>[c(D,{class:"product_img",src:y}),c(I,{class:"mgR10"},{default:s((()=>[c(I,{class:"product_value_label mgT10"},{default:s((()=>[r("A text description guiding the relighting and gener")])),_:1}),c(I,{class:"flex row justifyBetween product_value"},{default:s((()=>[c(I,null,{default:s((()=>[r(u(e.$t("18_Expiration_time")),1)])),_:1}),c(I,null,{default:s((()=>[r("2024.8.13")])),_:1})])),_:1}),c(I,{class:"flex row justifyBetween product_value"},{default:s((()=>[c(I,null,{default:s((()=>[r(u(e.$t("18_Visitors")),1)])),_:1}),c(I,null,{default:s((()=>[r("234")])),_:1})])),_:1}),c(I,{class:"flex row justifyBetween product_value"},{default:s((()=>[c(I,null,{default:s((()=>[r(u(e.$t("18_Runs")),1)])),_:1}),c(I,null,{default:s((()=>[r("13")])),_:1})])),_:1})])),_:1})])),_:1})])),_:1}),c(U,{xs:24,sm:12,md:12,lg:12,xl:12},{default:s((()=>[c(I,{class:"rightDiv pd20 borderbox"},{default:s((()=>[c(I,{class:"flex row justifyBetween card2_right_item"},{default:s((()=>[c(I,{class:"card2_right_label"},{default:s((()=>[A("span",{class:"card2_right_head"},u(e.$t("18_Preview"))+" URL:",1),r(" https://xxx.xxx.com.xxx… ")])),_:1}),c(I,{class:"card2_right_copy"},{default:s((()=>[r(u(e.$t("18_Copy_preview")),1)])),_:1})])),_:1}),c(I,{class:"flex justifyBetween mgT10 mgB10"},{default:s((()=>[c(I,{class:"flex column alignCenter option_item",onClick:l=>e.openHref(a.FileManager)},{default:s((()=>[c(D,{class:"option_img",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAoCAYAAABjPNNTAAAAAXNSR0IArs4c6QAAA4VJREFUWEe9mf9x2jAUx7+GBZIJGiYomaDi714hnqDNBIEJEiYInaBsYEyvf+cxQegEpROUDmDcPMnChljWU3HQXS53ifT80ff5/ZAc4ZSRKIUu+gA+APr3RfHDVrfIsUGEDXL8xA6EmOh/HhcFL0rUBTq4Q4RxBUhmxkATMkwR00a2CJBDGrj7Ak5qv2neXAorg0zUGF3cByvn2woru9Oqzpum+iFT9diievUsOWYY0cQF6oZk93aRAFA+QVr5f441dhggpu2xPTdkqp4R6Yg95yAMaSCDPIeLXVuvcf1rJZfqC4Bv55Tv1bMyTBDTzP79EDJRV+jiCcBVi5C/Adic+F6YIbbI0LPv5yFkquaI8LklwAW6mOIjrQ/sGU9xOmsWouL2EtKo+KsVwBxTjOjBacsUhidvYGa4ZDVLyPZUnGNItxrQ1HZWzaaxssqYFMeicL135U+92RJyqXjB6e9ihmvEtEaiboo8ewhgqgzP2SJVD4j0JlxjiyFdGkizYw6YU4c2qo0sFdtzFYIJhjRzbqRKkWFgIP07ksJvMKReAckR/a52oX1nZeJMDORSLQCMpCQN82SQEQb4RARJTs6RWiXbKoF+yGrky8TZWCX/CJOsT2wXJDcNU0RYawVNHHD79+gzyB2+hcwFk6tTVi/HhYV+aK5LqM0K9ZDHeVMOqJ8ZCsnliutq2aSmaoYId8UOXJCcdibo6s3wux/U/oW5O8PtHpAjswNVANqE7H8nA11Wdbc7XZRGy0qSKj7r1JW99iFzrOUpKEOMmBaexP8WkEUKWio+njZHmi13zYn/LSCn8rJolWze0ApDMkGxVO2ktciWRYnRspRx9/Jc24zYjfxQfWR6zmmDm5ER9aqtmr8jsd0y954d8HxOJxzZKx1INlG33PZVm15WiF3kHg3Hzv0id+SHq2pEKcqiXX6YmOuNum4dEtVHB+MWjx/7lHd8EPN3yyU612N7fuFKcnrDbG0bIfiiQB/g6o60/nQU7riwFdXKVgvJ5iRuD3usfHaOrxgRC7Uf7muW5vZf/tCQmRyYI7o+XtJ8YSU5doZANM9dIcNN2IVVSMSfClrjYpm7q7Oktw7hsKZj55Njw/BfotrFZZVp5xqG1dvhoc698nfStbMSlr84hOZG/iLBcDMJnEWQK1kH/V2pl08f3J3zZSsD8znbdunsyr9FwqeDQ1jga/EPycGA5AO24NoAAAAASUVORK5CYII="}),c(I,{class:"option_label"},{default:s((()=>[r("小程序")])),_:1})])),_:2},1032,["onClick"]),c(I,{class:"flex column alignCenter option_item",onClick:l=>e.openHref(a.FileManager)},{default:s((()=>[c(D,{class:"option_img",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAoCAYAAABjPNNTAAAAAXNSR0IArs4c6QAAAchJREFUWEftmF1OAjEQx2cW3njxBna5APQGeANJFPUNb6AnEE8ANyA+meyayA2IJ1jQA9Aj4Lt0zHYBd/kK7XY3JHYfy3Tm1/9MJ0wRdnxRwJoe4hgAznb9XsgagZALuuB3Qmz6x82F6JUxr4pRqYAriD2gGUgFWMExILBC1DrGaQwK1OYdMVmZryFPAvDvEHMp6Z7fiFG8tIacBn4ECM1jDluWjVzQI78VAwU5DVkfAB/KCq4TJwZNIN/qA5J0qbO5LFsC6m3d7rKC68RxkDpqHbJVSsbtx5bDIvwsb7dPRTi35dNBOiVtKWDLzz+sSYQ5SfhW/1wQzk9PSQQhK8R5W8xV731nzPvBmQ1Qa+mWBB+8M2uloaahnf7rIJ2SJsXuajKZcQxuYaonLie6SaMzy4wgk8DPDPqmvdP4dssq+by9/dpwqFSikLU8UC8jWp8xJCB1G1fiRSfaV8ieJGBPZ88yS4bpVruPBzUFzA+pJKFe41o8H1In71xvnu4M1X7Qz6A+JKSuborT9pYgtxWNhuysUvP6eQEtpTt95kTRGNCrqdc5K29LFpVMYIlohIDMFmABSuapvP17rStZBKaDtKWqU9KWkr/ig/6LG/FBRQAAAABJRU5ErkJggg=="}),c(I,{class:"option_label"},{default:s((()=>[r("下架")])),_:1})])),_:2},1032,["onClick"]),c(I,{class:"flex column alignCenter option_item",onClick:l=>e.openHref(a.FileManager)},{default:s((()=>[c(D,{class:"option_img",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAoCAYAAABjPNNTAAAAAXNSR0IArs4c6QAAAX5JREFUWEftWNFVwzAMvNsAJoARYAOYADaATsAI0A3YgI4AEwATwAYwQjcQudbhpU7sxCFN+ZDf608iWdezFMlH/GGZ2SmAJwAXA7Z5BrAguR5gu2PCUoemvZm9DgRYuy1JPpTGHA0ysPhVGHBN8rjQBy2QZnYE4A6AjlK/1JLdWWnAivm3Hh+lgxj/rO26QIqdHLgRuIpddhjvAmnFW+7BgVXy5ph0kENJzzI5dJM57UZ/gv4FSDM7SG42jzlZOPULB5nJlSmY1JDwEmJoqLiJ4q0AvIdnVwCuo/dLAN/hmXxbg8kUIH8HBDO7DRNQE4emHAFFldIaJO4jkJckN22x6v2yi/8kHGRgzJls1VviE+Q5Kaa8cLxwUh3KC8c7zvaqubnce++OCiV5ffDC8cLxwtlWiw8YhxowdKs7mVOpANApsua+k123vX1jXpFcxEFyIKXkfswsqJ43Fd5emSX0Zym+Eu/nUH6Ton+vqhYEfB29FAmxO/WqNfLH1MY/lY/nOJ6vCoIAAAAASUVORK5CYII="}),c(I,{class:"option_label"},{default:s((()=>[r("删除")])),_:1})])),_:2},1032,["onClick"])])),_:2},1024),c(I,{class:"flex justifyBetween mgT10 mgB10"},{default:s((()=>[c(I,{class:"flex alignCenter",onClick:l=>e.openHref(a.FileManager)},{default:s((()=>[c(I,{class:"option_btn"},{default:s((()=>[r("去除顶部广告")])),_:1})])),_:2},1032,["onClick"]),c(I,{class:"flex alignCenter",onClick:l=>e.openHref(a.FileManager)},{default:s((()=>[c(I,{class:"option_btn"},{default:s((()=>[r("编辑工作流")])),_:1})])),_:2},1032,["onClick"])])),_:2},1024)])),_:2},1024)])),_:2},1024)])),_:2},1024)))),128)),c(I,{class:"flex detail_item justifyCenter"},{default:s((()=>[c(I,{class:"skewDiv text2"},{default:s((()=>[c(I,{class:"skew"}),c(I,{class:"skewTitle"},{default:s((()=>[r(u(e.$t("18_Stencil")),1)])),_:1})])),_:1})])),_:1}),c(I,{class:"flex row wrap card2"},{default:s((()=>[c(I,{class:"flex row alignCenter card2_item"},{default:s((()=>[c(D,{class:"product_img",src:y}),c(I,{class:"flex column justifyStart alignStart product_value_item"},{default:s((()=>[c(I,{class:"product_value_label"},{default:s((()=>[r(u(e.$t("18_generates")),1)])),_:1})])),_:1})])),_:1}),c(I,{class:"flex row justifyBetween wrap card2_item2"},{default:s((()=>[c(I,{class:"flex row justifyBetween card2_right_item"},{default:s((()=>[c(I,{class:"card2_right_label"},{default:s((()=>[A("span",{class:"card2_right_head"},u(e.$t("18_Preview"))+" URL:",1),r(" https://xxx.xxx.com.xxx… ")])),_:1}),c(I,{class:"card2_right_copy"},{default:s((()=>[r(u(e.$t("18_Copy_preview")),1)])),_:1})])),_:1}),c(I,{class:"flex row justifyCenter card2_right_item"},{default:s((()=>[c(I,{class:"flex row justifyCenter alignCenter btn_div",onClick:a[4]||(a[4]=e=>J.goCreatePage())},{default:s((()=>[c(D,{class:"btn_img",src:j}),c(I,{class:"btn_text"},{default:s((()=>[r(u(e.$t("start")),1)])),_:1})])),_:1})])),_:1}),c(I)])),_:1})])),_:1})])),_:1})])),_:1})}],["__scopeId","data-v-a5994ab5"]]);export{J as default};
