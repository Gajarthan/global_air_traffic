# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_07:28:02_UTC-green)

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

**Latest saved flight:** 2026-08-14 07:28:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 07:28:02 UTC

- **194,437** saved flights
- **61,156** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **194,437** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,322,968.6 tonnes** estimated CO2 emissions
- **134,664,847 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7719 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3834 |
| 4 | IndiGo | 3353 |
| 5 | Southwest Airlines | 3031 |
| 6 | American Airlines | 3015 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1825 |
| 10 | AZU | 1752 |
| 11 | Lufthansa | 1674 |
| 12 | Vueling | 1615 |
| 13 | WIF | 1609 |
| 14 | LXJ | 1541 |
| 15 | easyJet | 1337 |
| 16 | Swiss International | 1317 |
| 17 | AXM | 1264 |
| 18 | QLK | 1201 |
| 19 | EJU | 1196 |
| 20 | All Nippon Airways | 1179 |
| 21 | Alaska Airlines | 1157 |
| 22 | VIV | 1071 |
| 23 | GLO | 1046 |
| 24 | PGT | 1012 |
| 25 | Air France | 1011 |
| 26 | AEE | 994 |
| 27 | United Airlines | 994 |
| 28 | CXK | 989 |
| 29 | WMT | 966 |
| 30 | Wizz Air | 962 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165680 |
| 2 | 🇪🇸 ES | 12514 |
| 3 | 🇧🇷 BR | 11177 |
| 4 | 🇦🇺 AU | 10962 |
| 5 | 🇨🇦 CA | 10656 |
| 6 | 🇮🇳 IN | 10494 |
| 7 | 🇮🇹 IT | 10091 |
| 8 | 🇩🇪 DE | 9595 |
| 9 | 🇬🇧 GB | 9075 |
| 10 | 🇯🇵 JP | 7929 |
| 11 | 🇫🇷 FR | 7735 |
| 12 | 🇨🇴 CO | 7569 |
| 13 | 🇬🇷 GR | 5687 |
| 14 | 🇲🇽 MX | 5509 |
| 15 | 🇹🇷 TR | 5248 |
| 16 | 🇨🇭 CH | 5223 |
| 17 | 🇳🇴 NO | 4977 |
| 18 | 🇲🇾 MY | 3313 |
| 19 | 🇿🇦 ZA | 3266 |
| 20 | 🇵🇱 PL | 3190 |
| 21 | 🇹🇭 TH | 3012 |
| 22 | 🇳🇿 NZ | 2734 |
| 23 | 🇵🇭 PH | 2568 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2361 |
| 26 | 🇭🇷 HR | 2014 |
| 27 | 🇲🇦 MA | 1971 |
| 28 | 🇳🇱 NL | 1742 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1566 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4053 |
| 2 | Denver International Airport |  | US | 3183 |
| 3 | Tokyo International Airport |  | JP | 2437 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2365 |
| 6 | Harry Reid International Airport |  | US | 2250 |
| 7 | Zurich Airport |  | CH | 2057 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2052 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2016 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1774 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1640 |
| 16 | Congonhas Airport |  | BR | 1627 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1527 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 20 | Capua Airport |  | IT | 1492 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1436 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1396 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1360 |
| 24 | Malpensa International Airport |  | IT | 1344 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Bengaluru International Airport |  | IN | 1238 |
| 28 | Kuala Lumpur International Airport |  | MY | 1234 |
| 29 | Ninoy Aquino International Airport |  | PH | 1216 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1215 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1161 |
| 33 | Viracopos International Airport |  | BR | 1128 |
| 34 | Seattle-Tacoma International Airport |  | US | 1120 |
| 35 | Calgary International Airport |  | CA | 1111 |
| 36 | Reno/Tahoe International Airport |  | US | 1104 |
| 37 | Oslo Gardermoen Airport |  | NO | 1092 |
| 38 | Daniel K Inouye International Airport |  | US | 1086 |
| 39 | Tenerife Norte Airport |  | ES | 1067 |
| 40 | Vitoria/Foronda Airport |  | ES | 1060 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 714 | 21m | 244 km | 3,006.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 471 | 1h 7m | 770 km | 6,256.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 451 | 24m | 225 km | 1,749.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 291 | 44m | 241 km | 1,208.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 242 | 27m | 215 km | 896.3 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 238 | 24m | 218 km | 896.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 229 | 1h 38m | 1,156 km | 4,568.5 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 221 | 31m | 369 km | 1,406.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 211 | 1h 3m | 695 km | 2,529.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-14 07:11 UTC | 2026-08-14 07:28 UTC | 16m |
| FJAPJ | FJA | Sterpenich Airport (EBAR) | Innsbruck Airport (LOWI) | 2026-08-14 05:14 UTC | 2026-08-14 07:27 UTC | 2h 13m |
| N842TS |  | St Gallen Altenrhein Airport (LSZR) | Friedrichshafen Airport (EDNY) | 2026-08-14 06:41 UTC | 2026-08-14 07:11 UTC | 30m |
| TOG132 | TOG | Modesto City-County-Harry Sham Field (KMOD) | Reno/Tahoe International Airport (KRNO) | 2026-08-14 06:38 UTC | 2026-08-14 07:10 UTC | 32m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Hausen am Albis Airport (LSZN) | 2026-08-14 06:48 UTC | 2026-08-14 07:00 UTC | 12m |
| PUJ | PUJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-14 06:35 UTC | 2026-08-14 06:58 UTC | 22m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-14 06:20 UTC | 2026-08-14 06:57 UTC | 37m |
| HLE27 | HLE | RAF Northolt (EGWU) | London City Airport (EGLC) | 2026-08-14 06:48 UTC | 2026-08-14 06:56 UTC | 7m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-08-14 06:12 UTC | 2026-08-14 06:51 UTC | 38m |
| N917SH |  | Joe Foss Field (KFSD) | Clark County Airport (K8D7) | 2026-08-14 06:26 UTC | 2026-08-14 06:48 UTC | 22m |
| N371LL |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Ontonagon County/Schuster Field (KOGM) | 2026-08-14 06:03 UTC | 2026-08-14 06:47 UTC | 43m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-14 05:50 UTC | 2026-08-14 06:44 UTC | 53m |
| OKAPT | OKA | Otrokovice Zlin Airport (LKOT) | Kunovice Airport (LKKU) | 2026-08-14 06:12 UTC | 2026-08-14 06:41 UTC | 28m |
| WIF3LP | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-08-14 05:45 UTC | 2026-08-14 06:39 UTC | 54m |
| JBU608 | JetBlue | Harry Reid International Airport (KLAS) | Double Eagle Ii Airport (KAEG) | 2026-08-14 05:37 UTC | 2026-08-14 06:35 UTC | 57m |
| HBKGP | HBK | Bern Belp Airport (LSZB) | Bern Belp Airport (LSZB) | 2026-08-14 06:07 UTC | 2026-08-14 06:34 UTC | 27m |
| RXA6673 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-08-14 05:50 UTC | 2026-08-14 06:34 UTC | 44m |
| GPMMC | GPM | Norwich International Airport (EGSH) | RAF Sculthorpe (EGUP) | 2026-08-14 06:13 UTC | 2026-08-14 06:32 UTC | 19m |
| EJU54ZC | EJU | Linate Airport (LIML) | Ibiza Airport (LEIB) | 2026-08-14 04:57 UTC | 2026-08-14 06:29 UTC | 1h 32m |
| RYR81NH | Ryanair | Malaga Airport (LEMG) | Ifrane Airport (GMFI) | 2026-08-14 05:59 UTC | 2026-08-14 06:27 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
