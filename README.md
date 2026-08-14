# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_12:16:06_UTC-green)

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

**Latest saved flight:** 2026-08-14 12:16:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 12:16:06 UTC

- **195,047** saved flights
- **61,340** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **195,047** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,330,961.3 tonnes** estimated CO2 emissions
- **135,128,190 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7764 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3835 |
| 4 | IndiGo | 3369 |
| 5 | Southwest Airlines | 3031 |
| 6 | American Airlines | 3015 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1825 |
| 10 | AZU | 1754 |
| 11 | Lufthansa | 1689 |
| 12 | Vueling | 1628 |
| 13 | WIF | 1613 |
| 14 | LXJ | 1542 |
| 15 | easyJet | 1346 |
| 16 | Swiss International | 1320 |
| 17 | AXM | 1275 |
| 18 | QLK | 1208 |
| 19 | EJU | 1207 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1071 |
| 23 | GLO | 1047 |
| 24 | Air France | 1025 |
| 25 | PGT | 1015 |
| 26 | AEE | 1002 |
| 27 | United Airlines | 994 |
| 28 | CXK | 990 |
| 29 | WMT | 974 |
| 30 | Wizz Air | 967 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165736 |
| 2 | 🇪🇸 ES | 12602 |
| 3 | 🇧🇷 BR | 11182 |
| 4 | 🇦🇺 AU | 11007 |
| 5 | 🇨🇦 CA | 10663 |
| 6 | 🇮🇳 IN | 10543 |
| 7 | 🇮🇹 IT | 10149 |
| 8 | 🇩🇪 DE | 9690 |
| 9 | 🇬🇧 GB | 9174 |
| 10 | 🇯🇵 JP | 7979 |
| 11 | 🇫🇷 FR | 7791 |
| 12 | 🇨🇴 CO | 7577 |
| 13 | 🇬🇷 GR | 5732 |
| 14 | 🇲🇽 MX | 5510 |
| 15 | 🇹🇷 TR | 5286 |
| 16 | 🇨🇭 CH | 5280 |
| 17 | 🇳🇴 NO | 5001 |
| 18 | 🇲🇾 MY | 3337 |
| 19 | 🇿🇦 ZA | 3294 |
| 20 | 🇵🇱 PL | 3216 |
| 21 | 🇹🇭 TH | 3030 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2583 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2031 |
| 27 | 🇲🇦 MA | 1981 |
| 28 | 🇳🇱 NL | 1759 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1577 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4053 |
| 2 | Denver International Airport |  | US | 3183 |
| 3 | Tokyo International Airport |  | JP | 2447 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2380 |
| 6 | Harry Reid International Airport |  | US | 2253 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2064 |
| 8 | Zurich Airport |  | CH | 2064 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2016 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1777 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1652 |
| 16 | Congonhas Airport |  | BR | 1627 |
| 17 | Madrid Barajas International Airport |  | ES | 1537 |
| 18 | Macau International Airport |  | MO | 1530 |
| 19 | Capua Airport |  | IT | 1494 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1437 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1398 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1350 |
| 25 | Charles de Gaulle International Airport |  | FR | 1339 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Kuala Lumpur International Airport |  | MY | 1243 |
| 28 | Bengaluru International Airport |  | IN | 1239 |
| 29 | Ninoy Aquino International Airport |  | PH | 1221 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1215 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1172 |
| 33 | Viracopos International Airport |  | BR | 1129 |
| 34 | Seattle-Tacoma International Airport |  | US | 1121 |
| 35 | Calgary International Airport |  | CA | 1112 |
| 36 | Reno/Tahoe International Airport |  | US | 1104 |
| 37 | Oslo Gardermoen Airport |  | NO | 1100 |
| 38 | Daniel K Inouye International Airport |  | US | 1086 |
| 39 | Tenerife Norte Airport |  | ES | 1068 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1067 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 714 | 21m | 244 km | 3,006.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 473 | 1h 7m | 770 km | 6,283.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 328 | 27m | 275 km | 1,554.3 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 291 | 44m | 241 km | 1,208.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 280 | 1h 49m | 1,423 km | 6,871.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 243 | 27m | 215 km | 900.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 239 | 24m | 218 km | 900.4 t |
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
| N66046 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-14 11:54 UTC | 2026-08-14 12:16 UTC | 21m |
| PGT79J | PGT | Sabiha Gokcen International Airport (LTFJ) | Trabzon International Airport (LTCG) | 2026-08-14 11:06 UTC | 2026-08-14 12:12 UTC | 1h 5m |
| DKAGZ | DKA | Norden-Norddeich Airport (EDWS) | Juist Airport (EDWJ) | 2026-08-14 11:44 UTC | 2026-08-14 12:02 UTC | 18m |
| CJT942 | CJT | Cincinnati/Northern Kentucky International Airport (KCVG) | John C. Munro Hamilton International Airport (CYHM) | 2026-08-14 11:07 UTC | 2026-08-14 12:01 UTC | 53m |
| N105HF |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-08-14 11:42 UTC | 2026-08-14 12:01 UTC | 18m |
| GFOXP | GFO | EG32 (EG32) | EG32 (EG32) | 2026-08-14 11:43 UTC | 2026-08-14 12:01 UTC | 17m |
| HBZZX | HBZ | Muenster Aero Airport (LSPU) | Meiringen Airport (LSMM) | 2026-08-14 11:00 UTC | 2026-08-14 11:59 UTC | 58m |
| MTU47 | MTU | Stones River Airport (7TN3) | Lebanon Municipal Airport (KM54) | 2026-08-14 11:37 UTC | 2026-08-14 11:55 UTC | 18m |
| N212BG |  | Federhart-Ophelia Airport (VA99) | Reedville Airport (VA98) | 2026-08-14 11:49 UTC | 2026-08-14 11:51 UTC | 2m |
| CAMEL1 | CAM | RAF Cranwell (EGYD) | EGYO (EGYO) | 2026-08-14 11:17 UTC | 2026-08-14 11:51 UTC | 34m |
| N53402 |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-08-14 11:48 UTC | 2026-08-14 11:49 UTC | 1m |
| HB2100 |  | Schanis Airport (LSZX) | Sion Airport (LSGS) | 2026-08-14 09:20 UTC | 2026-08-14 11:47 UTC | 2h 26m |
| DEUKS | DEU | Mainz-Finthen Airport (EDFZ) | Mainz-Finthen Airport (EDFZ) | 2026-08-14 11:22 UTC | 2026-08-14 11:40 UTC | 18m |
| GBWXA | GBW | Chichester/Goodwood Airport (EGHR) | Chichester/Goodwood Airport (EGHR) | 2026-08-14 11:18 UTC | 2026-08-14 11:37 UTC | 19m |
| N8380C |  | 16PA (16PA) | Rostraver Airport (KFWQ) | 2026-08-14 10:54 UTC | 2026-08-14 11:37 UTC | 43m |
| SVF665 | SVF | Visby Airport (ESSV) | Stockholm-Bromma Airport (ESSB) | 2026-08-14 11:07 UTC | 2026-08-14 11:35 UTC | 28m |
| N754FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-14 10:54 UTC | 2026-08-14 11:34 UTC | 39m |
| AUR205 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-14 11:21 UTC | 2026-08-14 11:33 UTC | 11m |
| N299SP |  | Park River - W C Skjerven Field (KY37) | Park River - W C Skjerven Field (KY37) | 2026-08-14 11:17 UTC | 2026-08-14 11:29 UTC | 12m |
| N733PN |  | Northeast Philadelphia Airport (KPNE) | Solberg/Hunterdon Airport (KN51) | 2026-08-14 10:55 UTC | 2026-08-14 11:26 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
