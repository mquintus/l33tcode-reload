# 332. Reconstruct Itinerary

<p>You are given a list of airline <code>tickets</code> where <code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.</p>

<p>All of the tickets belong to a man who departs from <code>&quot;JFK&quot;</code>, thus, the itinerary must begin with <code>&quot;JFK&quot;</code>. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.</p>

<ul>
	<li>For example, the itinerary <code>[&quot;JFK&quot;, &quot;LGA&quot;]</code> has a smaller lexical order than <code>[&quot;JFK&quot;, &quot;LGB&quot;]</code>.</li>
</ul>

<p>You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> tickets = [[&quot;MUC&quot;,&quot;LHR&quot;],[&quot;JFK&quot;,&quot;MUC&quot;],[&quot;SFO&quot;,&quot;SJC&quot;],[&quot;LHR&quot;,&quot;SFO&quot;]]
<strong>Output:</strong> [&quot;JFK&quot;,&quot;MUC&quot;,&quot;LHR&quot;,&quot;SFO&quot;,&quot;SJC&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg" style="width: 222px; height: 230px;" />
<pre>
<strong>Input:</strong> tickets = [[&quot;JFK&quot;,&quot;SFO&quot;],[&quot;JFK&quot;,&quot;ATL&quot;],[&quot;SFO&quot;,&quot;ATL&quot;],[&quot;ATL&quot;,&quot;JFK&quot;],[&quot;ATL&quot;,&quot;SFO&quot;]]
<strong>Output:</strong> [&quot;JFK&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;SFO&quot;]
<strong>Explanation:</strong> Another possible reconstruction is [&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;ATL&quot;,&quot;SFO&quot;] but it is larger in lexical order.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tickets.length &lt;= 300</code></li>
	<li><code>tickets[i].length == 2</code></li>
	<li><code>from<sub>i</sub>.length == 3</code></li>
	<li><code>to<sub>i</sub>.length == 3</code></li>
	<li><code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> consist of uppercase English letters.</li>
	<li><code>from<sub>i</sub> != to<sub>i</sub></code></li>
</ul>



Note: Some testcases do crash the leetcode solver, like
```
[["JFK","YZZ"], ["YZZ", "JFK"], ["JFK", "AAA"], ["AAA", "AAB"], ["AAB", "AAA"], ["AAA", "AAB"], ["AAB", "AAA"], ["AAA", "AAB"], ["AAB", "AAA"], ["AAA", "AAB"], ["AAB", "AAA"], ["AAA", "AAB"], ["AAB", "AAA"]]
```
(kudos to https://leetcode.com/c910335/ for finding a short one)
and 
```
[["JFK","XUD"],["XUD","KLF"],["KLF","HMH"],["HMH","RSW"],["RSW","JXK"],["JXK","UCN"],["UCN","MGJ"],["MGJ","BGI"],["BGI","SMF"],["SMF","FOX"],["FOX","DKI"],["DKI","OAK"],["OAK","GMA"],["GMA","TSW"],["TSW","JBU"],["JBU","JLE"],["JLE","MIA"],["MIA","DSJ"],["DSJ","MHK"],["MHK","GBT"],["GBT","CXM"],["CXM","NWA"],["NWA","AYI"],["AYI","SOL"],["SOL","PBI"],["PBI","PDX"],["PDX","FVA"],["FVA","OAK"],["OAK","LAS"],["LAS","PKH"],["PKH","JGO"],["JGO","UCN"],["UCN","KPL"],["KPL","SID"],["SID","ROM"],["ROM","WUC"],["WUC","CEE"],["CEE","SCM"],["SCM","KRK"],["KRK","BHH"],["BHH","PIT"],["PIT","CAU"],["CAU","JYW"],["JYW","CRI"],["CRI","ETL"],["ETL","LRU"],["LRU","CKW"],["CKW","MSP"],["MSP","YAG"],["YAG","KPL"],["KPL","VGN"],["VGN","TBA"],["TBA","SFO"],["SFO","QVC"],["QVC","NQX"],["NQX","SNA"],["SNA","HYW"],["HYW","CWP"],["CWP","HTQ"],["HTQ","FFL"],["FFL","BOS"],["BOS","SOL"],["SOL","MWS"],["MWS","MCO"],["MCO","DEW"],["DEW","LGG"],["LGG","OGK"],["OGK","FLL"],["FLL","QXS"],["QXS","RIE"],["RIE","DEQ"],["DEQ","OJP"],["OJP","XOQ"],["XOQ","ATL"],["ATL","MOU"],["MOU","HLQ"],["HLQ","BYB"],["BYB","SEA"],["SEA","KQY"],["KQY","LRU"],["LRU","BMN"],["BMN","FLE"],["FLE","CFJ"],["CFJ","NSO"],["NSO","OAK"],["OAK","BWG"],["BWG","ETJ"],["ETJ","FRU"],["FRU","PIT"],["PIT","JXK"],["JXK","OGK"],["OGK","WTV"],["WTV","VVE"],["VVE","VGN"],["VGN","DHG"],["DHG","XFQ"],["XFQ","JFK"],["JFK","QNP"],["QNP","XKE"],["XKE","ROM"],["ROM","TBA"],["TBA","BOS"],["BOS","HTQ"],["HTQ","YAI"],["YAI","NWA"],["NWA","QML"],["QML","KRK"],["KRK","KHF"],["KHF","STL"],["STL","XSG"],["XSG","LGG"],["LGG","TCK"],["TCK","WLF"],["WLF","EMK"],["EMK","XCN"],["XCN","XUD"],["XUD","DWM"],["DWM","XCN"],["XCN","BOS"],["BOS","MGJ"],["MGJ","KJT"],["KJT","VVE"],["VVE","HWY"],["HWY","TWS"],["TWS","JBU"],["JBU","ANO"],["ANO","SIQ"],["SIQ","KQY"],["KQY","RBN"],["RBN","JFK"],["JFK","OYH"],["OYH","XCN"],["XCN","SCM"],["SCM","MCI"],["MCI","JGO"],["JGO","LER"],["LER","DFW"],["DFW","NTD"],["NTD","XSG"],["XSG","YHU"],["YHU","JFK"],["JFK","CKW"],["CKW","KHF"],["KHF","KJT"],["KJT","KID"],["KID","VMT"],["VMT","XFQ"],["XFQ","HTQ"],["HTQ","DWM"],["DWM","HTQ"],["HTQ","PDX"],["PDX","MDW"],["MDW","AUS"],["AUS","QRF"],["QRF","LQU"],["LQU","XTL"],["XTL","WUC"],["WUC","YWT"],["YWT","OYH"],["OYH","CWP"],["CWP","MOU"],["MOU","HAM"],["HAM","BFQ"],["BFQ","ITX"],["ITX","HMH"],["HMH","GTR"],["GTR","XCN"],["XCN","BUF"],["BUF","MEN"],["MEN","WOJ"],["WOJ","HSE"],["HSE","CDD"],["CDD","RIE"],["RIE","LDY"],["LDY","IGB"],["IGB","ORT"],["ORT","OXQ"],["OXQ","MSG"],["MSG","DAJ"],["DAJ","CSJ"],["CSJ","ANC"],["ANC","SYT"],["SYT","FGV"],["FGV","YTY"],["YTY","CKW"],["CKW","WUC"],["WUC","IGB"],["IGB","FLL"],["FLL","OLP"],["OLP","XFQ"],["XFQ","JKF"],["JKF","WDL"],["WDL","BOS"],["BOS","BNA"],["BNA","QRF"],["QRF","CVG"],["CVG","OLP"],["OLP","IQC"],["IQC","RJK"],["RJK","XXH"],["XXH","MGJ"],["MGJ","WUC"],["WUC","JDD"],["JDD","YTY"],["YTY","FPE"],["FPE","SEA"],["SEA","ANO"],["ANO","MGH"],["MGH","ADV"],["ADV","EWR"],["EWR","BFQ"],["BFQ","WLF"],["WLF","NAD"],["NAD","FPE"],["FPE","VVE"],["VVE","WOJ"],["WOJ","WDD"],["WDD","DAJ"],["DAJ","JOG"],["JOG","BQH"],["BQH","BUF"],["BUF","BOS"],["BOS","DSJ"],["DSJ","HMH"],["HMH","ANC"],["ANC","LFK"],["LFK","KHF"],["KHF","BWI"],["BWI","XJS"],["XJS","RMB"],["RMB","ETJ"],["ETJ","TSW"],["TSW","VUW"],["VUW","OUL"],["OUL","XTL"],["XTL","VVE"],["VVE","BWG"],["BWG","ADV"],["ADV","SIQ"],["SIQ","MGJ"],["MGJ","SUX"],["SUX","JDD"],["JDD","HYW"],["HYW","JFK"],["JFK","ANO"],["ANO","CFJ"],["CFJ","WHT"],["WHT","LFK"],["LFK","QVA"],["QVA","GLB"],["GLB","PIT"],["PIT","HSE"],["HSE","BQK"],["BQK","SEA"],["SEA","BMN"],["BMN","GBT"],["GBT","DHG"],["DHG","YNM"],["YNM","UOA"],["UOA","RMB"],["RMB","QUL"],["QUL","MCI"],["MCI","MEN"],["MEN","JDR"],["JDR","GMA"],["GMA","CLE"],["CLE","YTY"],["YTY","OWP"],["OWP","HMH"],["HMH","DEW"],["DEW","IGN"],["IGN","WHT"],["WHT","ULM"],["ULM","BMB"],["BMB","SNA"],["SNA","XFQ"],["XFQ","PUQ"],["PUQ","VSL"],["VSL","HMH"],["HMH","KNB"],["KNB","ANC"],["ANC","ENG"],["ENG","OEY"],["OEY","LRS"],["LRS","MWM"],["MWM","ENG"],["ENG","ATL"],["ATL","KHF"],["KHF","BSY"],["BSY","TOJ"],["TOJ","LQF"],["LQF","SUX"],["SUX","VWQ"],["VWQ","JXP"],["JXP","VWQ"],["VWQ","VMT"],["VMT","JDR"],["JDR","XKU"],["XKU","JFK"]]
```
and
```
[["JFK","KLO"],["KLO","VRU"],["VRU","JFK"],["JFK","IWC"],["IWC","EXD"],["EXD","VMC"],["VMC","EWR"],["EWR","PDS"],["PDS","PIT"],["PIT","YSM"],["YSM","HKO"],["HKO","RSW"],["RSW","HFM"],["HFM","HMN"],["HMN","IEM"],["IEM","MED"],["MED","NGX"],["NGX","FLL"],["FLL","BYC"],["BYC","SFO"],["SFO","XVS"],["XVS","FUQ"],["FUQ","XBK"],["XBK","DHW"],["DHW","YJO"],["YJO","ODN"],["ODN","XQT"],["XQT","ARH"],["ARH","DTW"],["DTW","MEI"],["MEI","DTW"],["DTW","GPP"],["GPP","WIE"],["WIE","ICJ"],["ICJ","VYX"],["VYX","TLS"],["TLS","NUB"],["NUB","YSM"],["YSM","CSD"],["CSD","CTI"],["CTI","LTU"],["LTU","YAE"],["YAE","KMO"],["KMO","AIT"],["AIT","IWC"],["IWC","OJB"],["OJB","DFV"],["DFV","HSS"],["HSS","EAN"],["EAN","SRT"],["SRT","BUF"],["BUF","EUH"],["EUH","KTE"],["KTE","TPA"],["TPA","SMF"],["SMF","AKP"],["AKP","MMB"],["MMB","TPA"],["TPA","VTO"],["VTO","LBT"],["LBT","GPP"],["GPP","KLO"],["KLO","LAX"],["LAX","MIA"],["MIA","LBT"],["LBT","THM"],["THM","WIB"],["WIB","ORO"],["ORO","IAD"],["IAD","GDP"],["GDP","HMN"],["HMN","CVO"],["CVO","LBT"],["LBT","UGU"],["UGU","HNL"],["HNL","JNQ"],["JNQ","YJO"],["YJO","UGU"],["UGU","ERQ"],["ERQ","XMP"],["XMP","DFF"],["DFF","BWI"],["BWI","MDW"],["MDW","XQT"],["XQT","PBI"],["PBI","IND"],["IND","MJN"],["MJN","SFO"],["SFO","RGS"],["RGS","NVP"],["NVP","LAS"],["LAS","KMO"],["KMO","RSW"],["RSW","HEW"],["HEW","NAT"],["NAT","SJU"],["SJU","FLM"],["FLM","DHL"],["DHL","LPI"],["LPI","QCD"],["QCD","HEW"],["HEW","MFN"],["MFN","YBC"],["YBC","CTX"],["CTX","IWC"],["IWC","BNG"],["BNG","QSH"],["QSH","ANC"],["ANC","EQC"],["EQC","MFN"],["MFN","FBW"],["FBW","NML"],["NML","AUR"],["AUR","LAS"],["LAS","EQC"],["EQC","KKC"],["KKC","LAS"],["LAS","QHN"],["QHN","MDW"],["MDW","KTL"],["KTL","BMQ"],["BMQ","UUH"],["UUH","VTO"],["VTO","CLF"],["CLF","XWB"],["XWB","JWA"],["JWA","STL"],["STL","BPF"],["BPF","MBD"],["MBD","HJT"],["HJT","UYU"],["UYU","HPE"],["HPE","VTO"],["VTO","OJB"],["OJB","SJU"],["SJU","MSY"],["MSY","QWV"],["QWV","OUC"],["OUC","XOY"],["XOY","GPW"],["GPW","OSC"],["OSC","MGL"],["MGL","VRF"],["VRF","XBK"],["XBK","PHL"],["PHL","QAW"],["QAW","YYQ"],["YYQ","BVI"],["BVI","LGA"],["LGA","VLT"],["VLT","UJJ"],["UJJ","BWI"],["BWI","LBT"],["LBT","DTW"],["DTW","MJN"],["MJN","HSS"],["HSS","OHW"],["OHW","BMT"],["BMT","IWC"],["IWC","UJJ"],["UJJ","PDS"],["PDS","EGK"],["EGK","TLS"],["TLS","SIX"],["SIX","AOT"],["AOT","SSH"],["SSH","VGK"],["VGK","JSF"],["JSF","GDP"],["GDP","BOL"],["BOL","JGH"],["JGH","IWC"],["IWC","AOX"],["AOX","FRI"],["FRI","LWV"],["LWV","PDX"],["PDX","STL"],["STL","AIT"],["AIT","CSD"],["CSD","SIX"],["SIX","BUF"],["BUF","VDB"],["VDB","XOY"],["XOY","TBV"],["TBV","BNG"],["BNG","HWF"],["HWF","LPI"],["LPI","JCB"],["JCB","DUI"],["DUI","IIK"],["IIK","YBC"],["YBC","VYX"],["VYX","YNS"],["YNS","BQH"],["BQH","WRM"],["WRM","SCY"],["SCY","DFY"],["DFY","BLC"],["BLC","PHX"],["PHX","DFY"],["DFY","BOS"],["BOS","WIB"],["WIB","SEA"],["SEA","THM"],["THM","TTY"],["TTY","HEW"],["HEW","YSM"],["YSM","BNN"],["BNN","MGY"],["MGY","PAR"],["PAR","IRJ"],["IRJ","VDB"],["VDB","ANC"],["ANC","SAN"],["SAN","RDU"],["RDU","REF"],["REF","BWI"],["BWI","HNL"],["HNL","AAP"],["AAP","CVO"],["CVO","JIR"],["JIR","AIT"],["AIT","NEE"],["NEE","HIN"],["HIN","TPU"],["TPU","AHF"],["AHF","MSY"],["MSY","HFM"],["HFM","ATW"],["ATW","KKC"],["KKC","CFB"],["CFB","HPE"],["HPE","BPF"],["BPF","XWB"],["XWB","XVS"],["XVS","FKN"],["FKN","SMF"],["SMF","AIT"],["AIT","MDW"],["MDW","CRG"],["CRG","VRU"],["VRU","FGD"],["FGD","GJK"],["GJK","WSR"],["WSR","FLM"],["FLM","OFX"],["OFX","GVU"],["GVU","UGU"],["UGU","DFV"],["DFV","DEN"],["DEN","NRE"],["NRE","PDX"],["PDX","CWG"],["CWG","TLS"],["TLS","HSS"],["HSS","BQI"],["BQI","HSB"],["HSB","CGT"],["CGT","OFX"],["OFX","TBV"],["TBV","NAT"],["NAT","JGH"],["JGH","NBP"],["NBP","AIT"],["AIT","AKP"],["AKP","SRT"],["SRT","NBP"],["NBP","JGH"],["JGH","VDB"],["VDB","YXT"],["YXT","CLF"],["CLF","KKC"],["KKC","KLO"],["KLO","BWT"],["BWT","LBT"],["LBT","ODN"],["ODN","SMF"],["SMF","GHP"],["GHP","BQI"],["BQI","EXD"],["EXD","ODN"],["ODN","BWT"],["BWT","PDX"],["PDX","IRU"],["IRU","SMJ"],["SMJ","UBB"],["UBB","SIX"],["SIX","XVS"],["XVS","ATW"],["ATW","AAP"],["AAP","RDU"],["RDU","TBV"],["TBV","JCB"],["JCB","TBV"],["TBV","IWC"],["IWC","VTO"]]
```
![image](https://github.com/mquintus/l33tcode-reload/assets/515945/2e6b511e-d801-4f2f-a232-61793fc892c6)