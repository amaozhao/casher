import{l as e,a,k as l,r as t,c as s,w as n,i,o,d as c,e as r,x as u,A as d,t as f,v as _,f as m,h as A,F as p,j as g}from"./index-BnGBZ2Zx.js";import{_ as x,a as w}from"./uni-row.B7qYmqQ-.js";import{r as h}from"./uni-app.es.BAhmK03J.js";import{r as C}from"./httpUtil.DN75PITx.js";import{_ as b}from"./home.zzgta-u4.js";import{_ as j}from"./me2.D5gY6gCa.js";import{_ as v,a as B,b as y}from"./connect.CZokdgBA.js";import{_ as J}from"./speed.D2MJkbce.js";import{_ as U}from"./_plugin-vue_export-helper.BCo6x5W8.js";const R=U({data:()=>({arts:[],templates:[],containers:{},appStatusBarHeight:0,href:"https://uniapp.dcloud.io/component/README?id=uniui"}),onShow:function(){let{statusBarHeight:a}=e();a>0&&(this.appStatusBarHeight=40+a),C({url:"gpu/gpucloud-fetch/",method:"POST",data:{method:"get",url:"/api/capps"}}).then((e=>{var a,l;this.containers=null==(l=null==(a=e.data)?void 0:a.containers)?void 0:l[0],console.log("this.containers",this.containers)})),C({url:"flow/b_flows/",method:"GET"}).then((e=>{this.arts=e.data})),C({url:"flow/b_templates/",method:"GET"}).then((e=>{this.templates=e.data}))},methods:{goCreatePage(){},offShelf(e){C({url:"flow/b_flows/"+e.id+"/",method:"PUT"}).then((e=>{a({title:"下架成功",icon:"none"})}))},delShelf(e){C({url:"flow/b_flows/"+e.id+"/",method:"DELETE"}).then((e=>{a({title:"删除成功",icon:"none"})}))},remove(e){C({url:"flow/banner/",method:"PUT",data:{workflow_id:e.id}}).then((e=>{a({title:"去除成功",icon:"none"})}))},onLeftTab(){l({url:"/pages/index/index"})},onHomeTab(){l({url:"/pages/tob/tob13Index"})},onMeTab(){l({url:"/pages/tob/tob15Me"})}}},[["render",function(e,a,l,C,U,R){const E=g,S=i,k=h(t("uni-col"),x),I=h(t("uni-row"),w);return o(),s(S,{class:"flex column alignCenter bg_div"},{default:n((()=>[c(S,{class:"flex row justifyBetween alignCenter header_div",style:u("margin-top:"+U.appStatusBarHeight+"rpx")},{default:n((()=>[c(S,{class:"flex row alignCenter",onClick:a[0]||(a[0]=e=>R.onLeftTab())},{default:n((()=>[c(E,{class:"header_img",src:b}),c(S,{class:"title"},{default:n((()=>[r(" Deploy AI ")])),_:1})])),_:1}),c(S,{class:"flex row justifyCenter alignCenter tab_div"},{default:n((()=>[c(S,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[1]||(a[1]=e=>R.onHomeTab())},{default:n((()=>[c(E,{class:"tab_img",src:b}),c(S,{class:"tab_label"},{default:n((()=>[r(" complaint ")])),_:1})])),_:1}),c(S,{class:"flex column justifyCenter alignCenter tab_div_item",onClick:a[2]||(a[2]=e=>R.onMeTab())},{default:n((()=>[c(E,{class:"tab_img",src:j}),c(S,{class:"tab_label"},{default:n((()=>[r(" me ")])),_:1})])),_:1})])),_:1})])),_:1},8,["style"]),c(S,{class:"flex column alignCenter div_content"},{default:n((()=>[U.containers?(o(),s(S,{key:0,class:"text1"},{default:n((()=>[r("我的实例")])),_:1})):d("",!0),U.containers?(o(),s(S,{key:1,class:"flex row wrap card1"},{default:n((()=>[c(S,{class:"flex column justifyStart card1_item"},{default:n((()=>[c(S,{class:"card1_item_title"},{default:n((()=>[r(f(U.containers.Name),1),_("span",{class:"red"},"（"+f(U.containers.SubTitle)+"）",1)])),_:1}),c(S,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:n((()=>[c(S,{class:"card1_item_value"},{default:n((()=>[r(f(U.containers.GpuType),1)])),_:1}),c(S,{class:"flex column"},{default:n((()=>[c(S,{class:"card1_item_value2"},{default:n((()=>[_("span",{class:"color_green"},f(U.containers.VramGB),1),r(" 显存 ")])),_:1}),c(S,{class:"card1_item_value2"},{default:n((()=>[_("span",{class:"color_green"},f(U.containers.MemoryGB),1),r(" 空间 ")])),_:1})])),_:1})])),_:1}),c(S,{class:"flex row justifyBetween alignCenter card1_item_row"},{default:n((()=>[c(S,{class:"card1_item_value2"},{default:n((()=>[r(" 到期时间 ")])),_:1}),c(S,{class:"card1_item_value2"},{default:n((()=>[r(f(U.containers.EndTime),1)])),_:1})])),_:1})])),_:1}),c(S,{class:"flex column justifyBetween alignCenter card1_item"},{default:n((()=>[c(S,{class:"card1_item_btn"},{default:n((()=>[r(" 打开comfyUI ")])),_:1}),c(S,{class:"flex row option_btn_div"},{default:n((()=>[c(S,{class:"flex column alignCenter option_item"},{default:n((()=>[c(E,{class:"option_img",src:v}),c(S,{class:"option_label"},{default:n((()=>[r("文件管理")])),_:1})])),_:1}),c(S,{class:"flex column alignCenter option_item"},{default:n((()=>[c(E,{class:"option_img",src:B}),c(S,{class:"option_label"},{default:n((()=>[r("关机")])),_:1})])),_:1}),c(S,{class:"flex column alignCenter option_item"},{default:n((()=>[c(E,{class:"option_img",src:y}),c(S,{class:"option_label"},{default:n((()=>[r("释放")])),_:1})])),_:1})])),_:1})])),_:1})])),_:1})):d("",!0),c(S,{class:"text2"},{default:n((()=>[r(" 我的作品 ")])),_:1}),c(S,{class:"flex row justifyCenter alignCenter wrap btn_view"},{default:n((()=>[c(S,{class:"btn1"},{default:n((()=>[r(" 安装ComfyUI插件生成 ")])),_:1}),c(S,{class:"btn2"},{default:n((()=>[r(" 在线生成 ")])),_:1})])),_:1}),(o(!0),m(p,null,A(U.arts,(e=>(o(),s(I,{class:"card2"},{default:n((()=>[c(k,{xs:24,sm:24,md:12,lg:12,xl:12},{default:n((()=>[c(S,{class:"flex row justifyBetween alignCenter card2_item"},{default:n((()=>{var a;return[c(E,{class:"product_img",mode:"aspectFill",src:null==(a=e.images[0])?void 0:a.image},null,8,["src"]),c(S,{class:"flex column product_value_item"},{default:n((()=>[c(S,{class:"product_value_label"},{default:n((()=>[r(f(e.title),1)])),_:2},1024),c(S,{class:"flex row justifyBetween product_value"},{default:n((()=>[c(S,null,{default:n((()=>[r("发布时间")])),_:1}),c(S,null,{default:n((()=>[r(f(e.created),1)])),_:2},1024)])),_:2},1024),c(S,{class:"flex row justifyBetween product_value"},{default:n((()=>[c(S,null,{default:n((()=>[r("访问人数")])),_:1}),c(S,null,{default:n((()=>[r(f(e.view_count),1)])),_:2},1024)])),_:2},1024),c(S,{class:"flex row justifyBetween product_value"},{default:n((()=>[c(S,null,{default:n((()=>[r("运行次数")])),_:1}),c(S,null,{default:n((()=>[r(f(e.task_count),1)])),_:2},1024)])),_:2},1024)])),_:2},1024)]})),_:2},1024)])),_:2},1024),c(k,{xs:24,sm:24,md:12,lg:12,xl:12},{default:n((()=>[c(S,{class:"flex column justifyBetween card2_item2"},{default:n((()=>[c(S,{class:"flex row justifyBetween"},{default:n((()=>[c(S,{class:"card2_right_label"},{default:n((()=>[_("span",{class:"card2_right_head"},"预览URL:"),r(" "+f(e.preview_url),1)])),_:2},1024),c(S,{class:"card2_right_copy"},{default:n((()=>[r(" 复制预览 ")])),_:1})])),_:2},1024),c(S,{class:"flex row justifyBetween"},{default:n((()=>[c(S,{class:"flex column alignCenter option_item"},{default:n((()=>[c(E,{class:"option_img",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAoCAYAAABjPNNTAAAAAXNSR0IArs4c6QAAA4VJREFUWEe9mf9x2jAUx7+GBZIJGiYomaDi714hnqDNBIEJEiYInaBsYEyvf+cxQegEpROUDmDcPMnChljWU3HQXS53ifT80ff5/ZAc4ZSRKIUu+gA+APr3RfHDVrfIsUGEDXL8xA6EmOh/HhcFL0rUBTq4Q4RxBUhmxkATMkwR00a2CJBDGrj7Ak5qv2neXAorg0zUGF3cByvn2woru9Oqzpum+iFT9diievUsOWYY0cQF6oZk93aRAFA+QVr5f441dhggpu2xPTdkqp4R6Yg95yAMaSCDPIeLXVuvcf1rJZfqC4Bv55Tv1bMyTBDTzP79EDJRV+jiCcBVi5C/Adic+F6YIbbI0LPv5yFkquaI8LklwAW6mOIjrQ/sGU9xOmsWouL2EtKo+KsVwBxTjOjBacsUhidvYGa4ZDVLyPZUnGNItxrQ1HZWzaaxssqYFMeicL135U+92RJyqXjB6e9ihmvEtEaiboo8ewhgqgzP2SJVD4j0JlxjiyFdGkizYw6YU4c2qo0sFdtzFYIJhjRzbqRKkWFgIP07ksJvMKReAckR/a52oX1nZeJMDORSLQCMpCQN82SQEQb4RARJTs6RWiXbKoF+yGrky8TZWCX/CJOsT2wXJDcNU0RYawVNHHD79+gzyB2+hcwFk6tTVi/HhYV+aK5LqM0K9ZDHeVMOqJ8ZCsnliutq2aSmaoYId8UOXJCcdibo6s3wux/U/oW5O8PtHpAjswNVANqE7H8nA11Wdbc7XZRGy0qSKj7r1JW99iFzrOUpKEOMmBaexP8WkEUKWio+njZHmi13zYn/LSCn8rJolWze0ApDMkGxVO2ktciWRYnRspRx9/Jc24zYjfxQfWR6zmmDm5ER9aqtmr8jsd0y954d8HxOJxzZKx1INlG33PZVm15WiF3kHg3Hzv0id+SHq2pEKcqiXX6YmOuNum4dEtVHB+MWjx/7lHd8EPN3yyU612N7fuFKcnrDbG0bIfiiQB/g6o60/nQU7riwFdXKVgvJ5iRuD3usfHaOrxgRC7Uf7muW5vZf/tCQmRyYI7o+XtJ8YSU5doZANM9dIcNN2IVVSMSfClrjYpm7q7Oktw7hsKZj55Njw/BfotrFZZVp5xqG1dvhoc698nfStbMSlr84hOZG/iLBcDMJnEWQK1kH/V2pl08f3J3zZSsD8znbdunsyr9FwqeDQ1jga/EPycGA5AO24NoAAAAASUVORK5CYII="}),c(S,{class:"option_label"},{default:n((()=>[r("小程序")])),_:1})])),_:1}),c(S,{class:"flex column alignCenter option_item",onClick:a=>R.offShelf(e)},{default:n((()=>[c(E,{class:"option_img",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAoCAYAAABjPNNTAAAAAXNSR0IArs4c6QAAAchJREFUWEftmF1OAjEQx2cW3njxBna5APQGeANJFPUNb6AnEE8ANyA+meyayA2IJ1jQA9Aj4Lt0zHYBd/kK7XY3JHYfy3Tm1/9MJ0wRdnxRwJoe4hgAznb9XsgagZALuuB3Qmz6x82F6JUxr4pRqYAriD2gGUgFWMExILBC1DrGaQwK1OYdMVmZryFPAvDvEHMp6Z7fiFG8tIacBn4ECM1jDluWjVzQI78VAwU5DVkfAB/KCq4TJwZNIN/qA5J0qbO5LFsC6m3d7rKC68RxkDpqHbJVSsbtx5bDIvwsb7dPRTi35dNBOiVtKWDLzz+sSYQ5SfhW/1wQzk9PSQQhK8R5W8xV731nzPvBmQ1Qa+mWBB+8M2uloaahnf7rIJ2SJsXuajKZcQxuYaonLie6SaMzy4wgk8DPDPqmvdP4dssq+by9/dpwqFSikLU8UC8jWp8xJCB1G1fiRSfaV8ieJGBPZ88yS4bpVruPBzUFzA+pJKFe41o8H1In71xvnu4M1X7Qz6A+JKSuborT9pYgtxWNhuysUvP6eQEtpTt95kTRGNCrqdc5K29LFpVMYIlohIDMFmABSuapvP17rStZBKaDtKWqU9KWkr/ig/6LG/FBRQAAAABJRU5ErkJggg=="}),c(S,{class:"option_label"},{default:n((()=>[r("下架")])),_:1})])),_:2},1032,["onClick"]),c(S,{class:"flex column alignCenter option_item",onClick:a=>R.delShelf(e)},{default:n((()=>[c(E,{class:"option_img",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAoCAYAAABjPNNTAAAAAXNSR0IArs4c6QAAAX5JREFUWEftWNFVwzAMvNsAJoARYAOYADaATsAI0A3YgI4AEwATwAYwQjcQudbhpU7sxCFN+ZDf608iWdezFMlH/GGZ2SmAJwAXA7Z5BrAguR5gu2PCUoemvZm9DgRYuy1JPpTGHA0ysPhVGHBN8rjQBy2QZnYE4A6AjlK/1JLdWWnAivm3Hh+lgxj/rO26QIqdHLgRuIpddhjvAmnFW+7BgVXy5ph0kENJzzI5dJM57UZ/gv4FSDM7SG42jzlZOPULB5nJlSmY1JDwEmJoqLiJ4q0AvIdnVwCuo/dLAN/hmXxbg8kUIH8HBDO7DRNQE4emHAFFldIaJO4jkJckN22x6v2yi/8kHGRgzJls1VviE+Q5Kaa8cLxwUh3KC8c7zvaqubnce++OCiV5ffDC8cLxwtlWiw8YhxowdKs7mVOpANApsua+k123vX1jXpFcxEFyIKXkfswsqJ43Fd5emSX0Zym+Eu/nUH6Ton+vqhYEfB29FAmxO/WqNfLH1MY/lY/nOJ6vCoIAAAAASUVORK5CYII="}),c(S,{class:"option_label"},{default:n((()=>[r("删除")])),_:1})])),_:2},1032,["onClick"])])),_:2},1024),c(S,{class:"flex row justifyBetween"},{default:n((()=>[c(S,{class:"card2_right_btn",onClick:a=>R.remove(e)},{default:n((()=>[r(" 去除顶部广告 ")])),_:2},1032,["onClick"]),c(S,{class:"card2_right_btn"},{default:n((()=>[r(" 编辑工作流 ")])),_:1})])),_:2},1024)])),_:2},1024)])),_:2},1024)])),_:2},1024)))),256)),c(S,{class:"text2"},{default:n((()=>[r(" 模版 ")])),_:1}),(o(!0),m(p,null,A(U.templates,(e=>(o(),s(I,{class:"card2"},{default:n((()=>[c(k,{xs:24,sm:24,md:12,lg:12,xl:12},{default:n((()=>[c(S,{class:"flex row alignCenter card2_item"},{default:n((()=>[c(E,{class:"template_img",mode:"aspectFill",src:e.images[0].image},null,8,["src"]),c(S,{class:"flex column justifyStart alignStart product_value_item"},{default:n((()=>[c(S,{class:"product_value_label"},{default:n((()=>[r(f(e.title),1)])),_:2},1024)])),_:2},1024)])),_:2},1024)])),_:2},1024),c(k,{xs:24,sm:24,md:12,lg:12,xl:12},{default:n((()=>[c(S,{class:"flex column justifyBetween card3_item2"},{default:n((()=>[c(S,{class:"flex row justifyBetween"},{default:n((()=>[c(S,{class:"card2_right_label"},{default:n((()=>[_("span",{class:"card2_right_head"},"预览URL:"),r(" "+f(e.preview_url),1)])),_:2},1024),c(S,{class:"card2_right_copy"},{default:n((()=>[r(" 复制预览 ")])),_:1})])),_:2},1024),c(S,{class:"flex row justifyCenter"},{default:n((()=>[c(S,{class:"flex row justifyCenter alignCenter btn_div",onClick:a[3]||(a[3]=e=>R.goCreatePage())},{default:n((()=>[c(E,{class:"btn_img",src:J}),c(S,{class:"btn_text"},{default:n((()=>[r("立即启用")])),_:1})])),_:1})])),_:1})])),_:2},1024)])),_:2},1024)])),_:2},1024)))),256))])),_:1})])),_:1})}],["__scopeId","data-v-63e0ff63"]]);export{R as default};