# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_09:36:08_UTC-green)

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

**Latest saved flight:** 2026-08-07 09:36:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 09:36:08 UTC

- **174,962** saved flights
- **56,539** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,962** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,106,142.8 tonnes** estimated CO2 emissions
- **122,095,232 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6939 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3458 |
| 4 | IndiGo | 3064 |
| 5 | Southwest Airlines | 2755 |
| 6 | American Airlines | 2735 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2069 |
| 9 | LATAM Airlines | 1616 |
| 10 | Lufthansa | 1579 |
| 11 | AZU | 1545 |
| 12 | WIF | 1466 |
| 13 | Vueling | 1437 |
| 14 | LXJ | 1370 |
| 15 | AXM | 1193 |
| 16 | easyJet | 1191 |
| 17 | Swiss International | 1190 |
| 18 | QLK | 1081 |
| 19 | All Nippon Airways | 1068 |
| 20 | EJU | 1068 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 963 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 927 |
| 25 | GLO | 921 |
| 26 | AEE | 915 |
| 27 | United Airlines | 907 |
| 28 | Air France | 897 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150429 |
| 2 | 🇪🇸 ES | 11184 |
| 3 | 🇧🇷 BR | 9948 |
| 4 | 🇦🇺 AU | 9938 |
| 5 | 🇮🇳 IN | 9604 |
| 6 | 🇨🇦 CA | 9566 |
| 7 | 🇮🇹 IT | 9031 |
| 8 | 🇩🇪 DE | 8669 |
| 9 | 🇬🇧 GB | 8100 |
| 10 | 🇯🇵 JP | 7060 |
| 11 | 🇫🇷 FR | 6939 |
| 12 | 🇨🇴 CO | 6423 |
| 13 | 🇬🇷 GR | 5092 |
| 14 | 🇲🇽 MX | 5003 |
| 15 | 🇨🇭 CH | 4628 |
| 16 | 🇳🇴 NO | 4556 |
| 17 | 🇹🇷 TR | 4312 |
| 18 | 🇲🇾 MY | 3113 |
| 19 | 🇵🇱 PL | 2920 |
| 20 | 🇿🇦 ZA | 2834 |
| 21 | 🇹🇭 TH | 2588 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2320 |
| 24 | 🇬🇹 GT | 2227 |
| 25 | 🇰🇷 KR | 2197 |
| 26 | 🇲🇦 MA | 1760 |
| 27 | 🇭🇷 HR | 1702 |
| 28 | 🇲🇪 ME | 1600 |
| 29 | 🇳🇱 NL | 1575 |
| 30 | 🇲🇴 MO | 1506 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3606 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2203 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2135 |
| 6 | Harry Reid International Airport |  | US | 2089 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1902 |
| 8 | Zurich Airport |  | CH | 1852 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1829 |
| 10 | La Aurora Airport |  | GT | 1714 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1543 |
| 16 | Macau International Airport |  | MO | 1506 |
| 17 | Congonhas Airport |  | BR | 1439 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1366 |
| 20 | Madrid Barajas International Airport |  | ES | 1360 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1232 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1190 |
| 26 | Charles de Gaulle International Airport |  | FR | 1186 |
| 27 | Kuala Lumpur International Airport |  | MY | 1172 |
| 28 | Bengaluru International Airport |  | IN | 1142 |
| 29 | Ninoy Aquino International Airport |  | PH | 1091 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1084 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1079 |
| 32 | Barcelona International Airport |  | ES | 1034 |
| 33 | Daniel K Inouye International Airport |  | US | 1009 |
| 34 | Seattle-Tacoma International Airport |  | US | 1008 |
| 35 | Calgary International Airport |  | CA | 992 |
| 36 | Reno/Tahoe International Airport |  | US | 991 |
| 37 | Viracopos International Airport |  | BR | 990 |
| 38 | Oslo Gardermoen Airport |  | NO | 974 |
| 39 | Tenerife Norte Airport |  | ES | 965 |
| 40 | Amsterdam Airport Schiphol |  | NL | 949 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 403 | 1h 8m | 770 km | 5,353.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 322 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 264 | 44m | 241 km | 1,096.6 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 240 | 1h 48m | 1,423 km | 5,890.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 229 | 20m | 250 km | 989.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 224 | 26m | 215 km | 829.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 208 | 19m | 144 km | 517.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 198 | 24m | 218 km | 745.9 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 191 | 43m | 452 km | 1,488.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXJ603 | LXJ | Bern Belp Airport (LSZB) | Farnborough Airport (EGLF) | 2026-08-07 07:59 UTC | 2026-08-07 09:36 UTC | 1h 36m |
| FDX5384 | FDX | Charles de Gaulle International Airport (LFPG) | Trabzon International Airport (LTCG) | 2026-08-07 06:10 UTC | 2026-08-07 09:35 UTC | 3h 24m |
| CSN382 | China Southern | Brisbane International Airport (YBBN) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-08-07 00:50 UTC | 2026-08-07 09:26 UTC | 8h 36m |
| FHPCJ | FHP | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-07 09:07 UTC | 2026-08-07 09:19 UTC | 11m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-07 08:26 UTC | 2026-08-07 09:18 UTC | 51m |
| AFR18DC | Air France | Charles de Gaulle International Airport (LFPG) | Cagliari / Elmas Airport (LIEE) | 2026-08-07 07:37 UTC | 2026-08-07 09:17 UTC | 1h 40m |
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-07 07:45 UTC | 2026-08-07 09:11 UTC | 1h 25m |
| ZSCJI | ZSC | Grand Central Airport (FAGC) | Walkersons Field (FADU) | 2026-08-07 08:43 UTC | 2026-08-07 09:06 UTC | 23m |
| GAF939 | GAF | Cologne Bonn Airport (EDDK) | Leipzig Halle Airport (EDDP) | 2026-08-07 07:15 UTC | 2026-08-07 09:03 UTC | 1h 48m |
| LIFELN5 | LIF | West Pueblo Airport (7CO8) | Silver West Airport (KC08) | 2026-08-07 08:49 UTC | 2026-08-07 09:03 UTC | 14m |
| JAL2825 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-08-07 08:11 UTC | 2026-08-07 09:01 UTC | 49m |
| DLH63M | Lufthansa | Munich International Airport (EDDM) | Bilbao Airport (LEBB) | 2026-08-07 07:08 UTC | 2026-08-07 09:00 UTC | 1h 52m |
| AIC5DM | Air India | Indira Gandhi International Airport (VIDP) | Mysore Airport (VOMY) | 2026-08-07 06:37 UTC | 2026-08-07 09:00 UTC | 2h 23m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-08-07 08:36 UTC | 2026-08-07 09:00 UTC | 24m |
| G72234 |  | Laredo International Airport (KLRD) | Laredo International Airport (KLRD) | 2026-08-07 08:41 UTC | 2026-08-07 08:59 UTC | 18m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-07 08:44 UTC | 2026-08-07 08:58 UTC | 13m |
| EXS71CB | EXS | Glasgow International Airport (EGPF) | Faro Airport (LPFR) | 2026-08-07 06:05 UTC | 2026-08-07 08:57 UTC | 2h 52m |
| MVE4AX | MVE | Riga International Airport (EVRA) | Riga International Airport (EVRA) | 2026-08-07 08:14 UTC | 2026-08-07 08:56 UTC | 42m |
| AXM6494 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-08-07 08:42 UTC | 2026-08-07 08:55 UTC | 13m |
| TCCFD | TCC | Ataturk International Airport (LTBA) | Kars Airport (LTCF) | 2026-08-07 07:24 UTC | 2026-08-07 08:54 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
