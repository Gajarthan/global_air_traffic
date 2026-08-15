# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_23:57:41_UTC-green)

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

**Latest saved flight:** 2026-08-14 23:57:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 23:57:41 UTC

- **197,186** saved flights
- **61,870** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,186** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,354,315.1 tonnes** estimated CO2 emissions
- **136,482,037 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7836 |
| 2 | SkyWest Airlines | 7104 |
| 3 | EJA | 3893 |
| 4 | IndiGo | 3388 |
| 5 | Southwest Airlines | 3060 |
| 6 | American Airlines | 3053 |
| 7 | ENY | 2444 |
| 8 | Delta Air Lines | 2336 |
| 9 | LATAM Airlines | 1854 |
| 10 | AZU | 1789 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1568 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1277 |
| 18 | EJU | 1222 |
| 19 | QLK | 1209 |
| 20 | All Nippon Airways | 1187 |
| 21 | Alaska Airlines | 1167 |
| 22 | VIV | 1086 |
| 23 | GLO | 1069 |
| 24 | Air France | 1034 |
| 25 | PGT | 1025 |
| 26 | AEE | 1012 |
| 27 | United Airlines | 1007 |
| 28 | CXK | 1005 |
| 29 | WMT | 986 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167860 |
| 2 | 🇪🇸 ES | 12718 |
| 3 | 🇧🇷 BR | 11370 |
| 4 | 🇦🇺 AU | 11029 |
| 5 | 🇨🇦 CA | 10806 |
| 6 | 🇮🇳 IN | 10592 |
| 7 | 🇮🇹 IT | 10271 |
| 8 | 🇩🇪 DE | 9772 |
| 9 | 🇬🇧 GB | 9252 |
| 10 | 🇯🇵 JP | 7996 |
| 11 | 🇫🇷 FR | 7843 |
| 12 | 🇨🇴 CO | 7781 |
| 13 | 🇬🇷 GR | 5786 |
| 14 | 🇲🇽 MX | 5583 |
| 15 | 🇹🇷 TR | 5371 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5041 |
| 18 | 🇲🇾 MY | 3342 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3252 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2747 |
| 23 | 🇵🇭 PH | 2595 |
| 24 | 🇬🇹 GT | 2528 |
| 25 | 🇰🇷 KR | 2388 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1993 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1586 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4115 |
| 2 | Denver International Airport |  | US | 3213 |
| 3 | Tokyo International Airport |  | JP | 2453 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2393 |
| 6 | Harry Reid International Airport |  | US | 2265 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2079 |
| 8 | Zurich Airport |  | CH | 2079 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2045 |
| 10 | La Aurora Airport |  | GT | 1937 |
| 11 | El Dorado International Airport |  | CO | 1807 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1763 |
| 13 | Salt Lake City International Airport |  | US | 1752 |
| 14 | Chicago O'Hare International Airport |  | US | 1735 |
| 15 | Congonhas Airport |  | BR | 1663 |
| 16 | Frankfurt am Main International Airport |  | DE | 1663 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1506 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1504 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1456 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Malpensa International Airport |  | IT | 1369 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1365 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1246 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1231 |
| 30 | Ninoy Aquino International Airport |  | PH | 1227 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1207 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1150 |
| 34 | Seattle-Tacoma International Airport |  | US | 1136 |
| 35 | Calgary International Airport |  | CA | 1122 |
| 36 | Reno/Tahoe International Airport |  | US | 1114 |
| 37 | Oslo Gardermoen Airport |  | NO | 1110 |
| 38 | Daniel K Inouye International Airport |  | US | 1094 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 722 | 21m | 244 km | 3,040.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 454 | 24m | 225 km | 1,761.3 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 280 | 22m | 55 km | 266.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 243 | 24m | 218 km | 915.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 241 | 19m | 99 km | 412.8 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 233 | 1h 38m | 1,156 km | 4,648.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 223 | 31m | 369 km | 1,419.5 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 48m | 1,304 km | 4,814.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N567FL |  | Trenton Mercer Airport (KTTN) | 19PA (19PA) | 2026-08-14 22:51 UTC | 2026-08-14 23:57 UTC | 1h 6m |
| CGECG | CGE | Vancouver International Airport (CYVR) | Harry Reid International Airport (KLAS) | 2026-08-14 20:23 UTC | 2026-08-14 23:57 UTC | 3h 33m |
| N9114D |  | OI34 (OI34) | OI34 (OI34) | 2026-08-14 23:49 UTC | 2026-08-14 23:55 UTC | 5m |
| N208GG |  | Penn Yan/Yates County Airport (KPEO) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-14 23:28 UTC | 2026-08-14 23:51 UTC | 23m |
| ZJH | ZJH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-14 23:28 UTC | 2026-08-14 23:49 UTC | 20m |
| N172JK |  | Shreveport Downtown Airport (KDTN) | Di's Cajun Restaurant Airport (LA52) | 2026-08-14 23:37 UTC | 2026-08-14 23:49 UTC | 11m |
| TKR181 | TKR | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-14 23:36 UTC | 2026-08-14 23:47 UTC | 10m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-08-14 23:24 UTC | 2026-08-14 23:46 UTC | 21m |
| N2028W |  | Oakdale Airport (KO27) | Visalia Municipal Airport (KVIS) | 2026-08-14 23:04 UTC | 2026-08-14 23:45 UTC | 41m |
| VHJKM | VHJ | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-14 23:08 UTC | 2026-08-14 23:40 UTC | 32m |
| EPI119 | EPI | Addison Airport (KADS) | Addison Airport (KADS) | 2026-08-14 22:14 UTC | 2026-08-14 23:34 UTC | 1h 20m |
| PKSNH | PKS | Pondok Cabe Air Base (WIHP) | Halim Perdanakusuma International Airport (WIHH) | 2026-08-14 23:22 UTC | 2026-08-14 23:34 UTC | 12m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-14 22:52 UTC | 2026-08-14 23:33 UTC | 40m |
| 231166 |  | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-08-14 22:26 UTC | 2026-08-14 23:32 UTC | 1h 5m |
| TKR138 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Big Muddy Ranch Airport (2OR1) | 2026-08-14 23:18 UTC | 2026-08-14 23:29 UTC | 11m |
| N335FB |  | Brookeridge Air Park (LL22) | 3IL2 (3IL2) | 2026-08-14 23:13 UTC | 2026-08-14 23:28 UTC | 15m |
| TKR01 | TKR | Throckmorton Municipal Airport (K72F) | Albany Municipal Airport (KT23) | 2026-08-14 22:04 UTC | 2026-08-14 23:27 UTC | 1h 22m |
|  |  | Round Mountain Ranch Airport (CA09) | Butte Valley Airport (KA32) | 2026-08-14 22:16 UTC | 2026-08-14 23:26 UTC | 1h 10m |
| LDACE21 | LDA | Chemehuevi Valley Airport (K49X) | Lake Havasu City Airport (KHII) | 2026-08-14 23:10 UTC | 2026-08-14 23:24 UTC | 13m |
| N20143 |  | Fairfield County Airport (KLHQ) | Fairfield County Airport (KLHQ) | 2026-08-14 22:49 UTC | 2026-08-14 23:24 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
