# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_06:24:50_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-14 06:24:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 06:24:50 UTC

- **109,708** saved flights
- **38,314** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,708** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,341,047.7 tonnes** estimated CO2 emissions
- **77,741,897 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4516 |
| 2 | SkyWest Airlines | 4110 |
| 3 | IndiGo | 2163 |
| 4 | EJA | 2107 |
| 5 | American Airlines | 1732 |
| 6 | Southwest Airlines | 1647 |
| 7 | ENY | 1362 |
| 8 | Delta Air Lines | 1295 |
| 9 | Lufthansa | 1243 |
| 10 | Vueling | 1006 |
| 11 | LATAM Airlines | 969 |
| 12 | WIF | 961 |
| 13 | AXM | 931 |
| 14 | AZU | 906 |
| 15 | LXJ | 828 |
| 16 | Swiss International | 794 |
| 17 | All Nippon Airways | 762 |
| 18 | Alaska Airlines | 749 |
| 19 | QLK | 726 |
| 20 | easyJet | 706 |
| 21 | EJU | 697 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 622 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 606 |
| 27 | MXY | 586 |
| 28 | CXK | 576 |
| 29 | AXB | 542 |
| 30 | Japan Airlines | 539 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92274 |
| 2 | 🇪🇸 ES | 7531 |
| 3 | 🇮🇳 IN | 6824 |
| 4 | 🇦🇺 AU | 6559 |
| 5 | 🇧🇷 BR | 6053 |
| 6 | 🇩🇪 DE | 5878 |
| 7 | 🇮🇹 IT | 5860 |
| 8 | 🇨🇦 CA | 5750 |
| 9 | 🇯🇵 JP | 4990 |
| 10 | 🇬🇧 GB | 4676 |
| 11 | 🇫🇷 FR | 4376 |
| 12 | 🇨🇴 CO | 3759 |
| 13 | 🇲🇽 MX | 3267 |
| 14 | 🇬🇷 GR | 3121 |
| 15 | 🇳🇴 NO | 3025 |
| 16 | 🇨🇭 CH | 2812 |
| 17 | 🇲🇾 MY | 2396 |
| 18 | 🇹🇷 TR | 2150 |
| 19 | 🇿🇦 ZA | 1871 |
| 20 | 🇰🇷 KR | 1838 |
| 21 | 🇹🇭 TH | 1812 |
| 22 | 🇳🇿 NZ | 1805 |
| 23 | 🇵🇱 PL | 1803 |
| 24 | 🇵🇭 PH | 1608 |
| 25 | 🇬🇹 GT | 1570 |
| 26 | 🇲🇦 MA | 1204 |
| 27 | 🇲🇴 MO | 1149 |
| 28 | 🇳🇱 NL | 1075 |
| 29 | 🇲🇪 ME | 1065 |
| 30 | 🇭🇷 HR | 955 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2354 |
| 2 | Denver International Airport |  | US | 1860 |
| 3 | Tokyo International Airport |  | JP | 1653 |
| 4 | Indira Gandhi International Airport |  | IN | 1483 |
| 5 | Guaymaral Airport |  | CO | 1393 |
| 6 | Harry Reid International Airport |  | US | 1388 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1369 |
| 8 | Zurich Airport |  | CH | 1240 |
| 9 | Frankfurt am Main International Airport |  | DE | 1224 |
| 10 | La Aurora Airport |  | GT | 1208 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1173 |
| 12 | Macau International Airport |  | MO | 1149 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1088 |
| 16 | Madrid Barajas International Airport |  | ES | 957 |
| 17 | Capua Airport |  | IT | 942 |
| 18 | Kuala Lumpur International Airport |  | MY | 937 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 930 |
| 20 | Salt Lake City International Airport |  | US | 927 |
| 21 | Charlotte/Douglas International Airport |  | US | 845 |
| 22 | Congonhas Airport |  | BR | 838 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 826 |
| 25 | Bengaluru International Airport |  | IN | 826 |
| 26 | Malpensa International Airport |  | IT | 801 |
| 27 | Ninoy Aquino International Airport |  | PH | 740 |
| 28 | Daniel K Inouye International Airport |  | US | 734 |
| 29 | General Edward Lawrence Logan International Airport |  | US | 729 |
| 30 | Tenerife Norte Airport |  | ES | 728 |
| 31 | Barcelona International Airport |  | ES | 720 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 714 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Amsterdam Airport Schiphol |  | NL | 665 |
| 35 | Don Mueang International Airport |  | TH | 660 |
| 36 | Vitoria/Foronda Airport |  | ES | 649 |
| 37 | Calgary International Airport |  | CA | 647 |
| 38 | Seattle-Tacoma International Airport |  | US | 630 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 629 |
| 40 | Viracopos International Airport |  | BR | 620 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 577 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 402 | 21m | 244 km | 1,692.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 284 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 269 | 1h 25m | 910 km | 4,221.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 258 | 1h 10m | 770 km | 3,427.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 163 | 20m | 99 km | 279.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 152 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 146 | 44m | 452 km | 1,137.9 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 143 | 18m | 144 km | 355.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 133 | 44m | 241 km | 552.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 131 | 1h 43m | 1,423 km | 3,214.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 131 | 1h 39m | 1,156 km | 2,613.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 123 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 122 | 24m | 223 km | 469.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RAM221M | Royal Air Maroc | Pskov Airport (ULOO) | Khrabrovo Airport (UMKK) | 2026-06-14 06:06 UTC | 2026-06-14 06:24 UTC | 18m |
| KLM96L | KLM Royal Dutch | Edinburgh Airport (EGPH) | Amsterdam Airport Schiphol (EHAM) | 2026-06-14 05:18 UTC | 2026-06-14 06:20 UTC | 1h 2m |
| FIA5582 | FIA | Tbilisi International Airport (UGTB) | Bacau Airport (LRBC) | 2026-06-13 22:12 UTC | 2026-06-14 06:18 UTC | 8h 5m |
| DFIDI | DFI | Hajduszoboszlo Airport (LHHO) | Hajduszoboszlo Airport (LHHO) | 2026-06-14 06:05 UTC | 2026-06-14 06:15 UTC | 9m |
| ACA59 | Air Canada | Toronto Pearson International Airport (CYYZ) | Nanki Shirahama Airport (RJBD) | 2026-06-13 17:39 UTC | 2026-06-14 06:09 UTC | 12h 30m |
| DAL1533 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-06-14 05:11 UTC | 2026-06-14 06:09 UTC | 57m |
| TGW420 | TGW | Singapore Changi International Airport (WSSS) | Malacca Airport (WMKM) | 2026-06-14 05:32 UTC | 2026-06-14 06:02 UTC | 30m |
| COOP92 | COO | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-06-14 05:38 UTC | 2026-06-14 05:52 UTC | 14m |
| EZS46NT | EZS | Geneva Cointrin International Airport (LSGG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-06-14 04:58 UTC | 2026-06-14 05:52 UTC | 54m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-14 05:25 UTC | 2026-06-14 05:52 UTC | 27m |
| AE998 |  | Tamworth Airport (YSTW) | Coonabarabran Airport (YCBB) | 2026-06-14 05:14 UTC | 2026-06-14 05:46 UTC | 31m |
| ASL120 | ASL | Belgrade Nikola Tesla Airport (LYBE) | Mińsk Mazowiecki Military Air Base (EPMM) | 2026-06-14 04:39 UTC | 2026-06-14 05:46 UTC | 1h 6m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-06-14 04:56 UTC | 2026-06-14 05:44 UTC | 48m |
| SAS62Y | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Kalixfors Airport (ESUK) | 2026-06-14 04:29 UTC | 2026-06-14 05:37 UTC | 1h 7m |
| IMVRK | IMV | Alzate Brianza Airport (LILB) | Sondrio Caiolo Airport (LILO) | 2026-06-14 05:13 UTC | 2026-06-14 05:36 UTC | 23m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-06-14 04:45 UTC | 2026-06-14 05:33 UTC | 47m |
| KNP973 | KNP | Suwon Airport (RKSW) | Incheon International Airport (RKSI) | 2026-06-14 05:13 UTC | 2026-06-14 05:31 UTC | 17m |
| NYT677 | NYT | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-06-14 05:25 UTC | 2026-06-14 05:31 UTC | 5m |
| TGW484 | TGW | Changi Air Base (WSAC) | Jendarata Airport (WMAJ) | 2026-06-14 04:52 UTC | 2026-06-14 05:30 UTC | 37m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-06-14 04:48 UTC | 2026-06-14 05:30 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
