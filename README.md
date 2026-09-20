# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_06:07:17_UTC-green)

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

**Latest saved flight:** 2026-09-20 06:07:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 06:07:17 UTC

- **264,222** saved flights
- **77,990** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,222** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,202,394.0 tonnes** estimated CO2 emissions
- **185,646,031 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10454 |
| 2 | SkyWest Airlines | 9187 |
| 3 | EJA | 5136 |
| 4 | IndiGo | 4445 |
| 5 | American Airlines | 4133 |
| 6 | Southwest Airlines | 3887 |
| 7 | Delta Air Lines | 3290 |
| 8 | ENY | 3114 |
| 9 | LATAM Airlines | 2551 |
| 10 | AZU | 2486 |
| 11 | Vueling | 2216 |
| 12 | WIF | 2128 |
| 13 | LXJ | 2070 |
| 14 | Lufthansa | 2033 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1742 |
| 17 | QLK | 1707 |
| 18 | EJU | 1665 |
| 19 | AXM | 1661 |
| 20 | United Airlines | 1620 |
| 21 | Alaska Airlines | 1567 |
| 22 | All Nippon Airways | 1524 |
| 23 | PGT | 1486 |
| 24 | WMT | 1485 |
| 25 | GLO | 1471 |
| 26 | Air France | 1445 |
| 27 | VIV | 1444 |
| 28 | Wizz Air | 1433 |
| 29 | CXK | 1279 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219546 |
| 2 | 🇪🇸 ES | 16635 |
| 3 | 🇧🇷 BR | 15470 |
| 4 | 🇦🇺 AU | 15137 |
| 5 | 🇨🇦 CA | 14712 |
| 6 | 🇮🇹 IT | 14367 |
| 7 | 🇮🇳 IN | 14049 |
| 8 | 🇩🇪 DE | 12751 |
| 9 | 🇬🇧 GB | 12253 |
| 10 | 🇨🇴 CO | 11995 |
| 11 | 🇫🇷 FR | 10550 |
| 12 | 🇯🇵 JP | 10220 |
| 13 | 🇹🇷 TR | 8006 |
| 14 | 🇬🇷 GR | 7663 |
| 15 | 🇲🇽 MX | 7270 |
| 16 | 🇨🇭 CH | 7048 |
| 17 | 🇳🇴 NO | 6516 |
| 18 | 🇹🇭 TH | 4738 |
| 19 | 🇲🇾 MY | 4478 |
| 20 | 🇿🇦 ZA | 4442 |
| 21 | 🇵🇱 PL | 4351 |
| 22 | 🇳🇿 NZ | 3678 |
| 23 | 🇵🇭 PH | 3519 |
| 24 | 🇬🇹 GT | 3366 |
| 25 | 🇭🇷 HR | 3013 |
| 26 | 🇰🇷 KR | 2999 |
| 27 | 🇲🇦 MA | 2645 |
| 28 | 🇲🇪 ME | 2476 |
| 29 | 🇳🇱 NL | 2367 |
| 30 | 🇮🇩 ID | 2218 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5399 |
| 2 | Denver International Airport |  | US | 4275 |
| 3 | Indira Gandhi International Airport |  | IN | 3176 |
| 4 | Tokyo International Airport |  | JP | 3053 |
| 5 | Harry Reid International Airport |  | US | 2812 |
| 6 | El Dorado International Airport |  | CO | 2811 |
| 7 | Guaymaral Airport |  | CO | 2785 |
| 8 | Zurich Airport |  | CH | 2747 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2654 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2558 |
| 11 | La Aurora Airport |  | GT | 2557 |
| 12 | Salt Lake City International Airport |  | US | 2330 |
| 13 | Chicago O'Hare International Airport |  | US | 2270 |
| 14 | Congonhas Airport |  | BR | 2255 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2158 |
| 16 | Capua Airport |  | IT | 2067 |
| 17 | Madrid Barajas International Airport |  | ES | 2039 |
| 18 | Frankfurt am Main International Airport |  | DE | 2016 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1996 |
| 20 | Malpensa International Airport |  | IT | 1904 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1891 |
| 22 | Charles de Gaulle International Airport |  | FR | 1865 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1860 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1836 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1804 |
| 26 | Macau International Airport |  | MO | 1760 |
| 27 | Ninoy Aquino International Airport |  | PH | 1728 |
| 28 | Barcelona International Airport |  | ES | 1648 |
| 29 | Charlotte/Douglas International Airport |  | US | 1647 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1625 |
| 31 | Kuala Lumpur International Airport |  | MY | 1605 |
| 32 | Viracopos International Airport |  | BR | 1603 |
| 33 | Seattle-Tacoma International Airport |  | US | 1552 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1541 |
| 35 | Calgary International Airport |  | CA | 1507 |
| 36 | Don Mueang International Airport |  | TH | 1503 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1486 |
| 39 | Vancouver International Airport |  | CA | 1479 |
| 40 | Antalya International Airport |  | TR | 1417 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 989 | 21m | 244 km | 4,164.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 725 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 664 | 1h 6m | 770 km | 8,820.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 430 | 44m | 555 km | 4,117.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 425 | 27m | 275 km | 2,013.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 418 | 1h 50m | 1,423 km | 10,258.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 379 | 24m | 218 km | 1,427.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 286 | 1h 50m | 1,304 km | 6,434.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 285 | 42m | 535 km | 2,632.2 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 266 | 18m | 14 km | 66.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8DA |  | Mc Clellan-Palomar Airport (KCRQ) | Van Nuys Airport (KVNY) | 2026-09-20 05:33 UTC | 2026-09-20 06:07 UTC | 34m |
| E7GPS |  | Banja Luka International Airport (LQBK) | Belgrade Nikola Tesla Airport (LYBE) | 2026-09-20 05:23 UTC | 2026-09-20 05:50 UTC | 26m |
| UAE394 | Emirates | Dubai International Airport (OMDB) | Naypyidaw Airport (VYEL) | 2026-09-20 01:00 UTC | 2026-09-20 05:44 UTC | 4h 43m |
| N135ED |  | Wings Field (KLOM) | Northeast Philadelphia Airport (KPNE) | 2026-09-20 05:31 UTC | 2026-09-20 05:39 UTC | 7m |
| CGE95 | CGE | Nelson Airport (NZNS) | Takaka Airport (NZTK) | 2026-09-20 04:38 UTC | 2026-09-20 05:28 UTC | 49m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-19 14:19 UTC | 2026-09-20 05:21 UTC | 15h 2m |
| GNS112 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-09-20 05:07 UTC | 2026-09-20 05:21 UTC | 14m |
| BDOG200 | BDO | RAAF Base Richmond (YSRI) | Bunyan Airfield (YBUY) | 2026-09-20 04:42 UTC | 2026-09-20 05:17 UTC | 35m |
| RYR53RZ | Ryanair | Václav Havel Airport (LKPR) | Otocac Airport (LDRO) | 2026-09-20 04:23 UTC | 2026-09-20 05:13 UTC | 50m |
| QLK1299 | QLK | Woodville Airport (YWVL) | Melbourne International Airport (YMML) | 2026-09-20 03:27 UTC | 2026-09-20 05:13 UTC | 1h 45m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-19 16:37 UTC | 2026-09-20 05:13 UTC | 12h 36m |
| RYR161N | Ryanair | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-09-20 03:55 UTC | 2026-09-20 05:12 UTC | 1h 17m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-09-20 04:29 UTC | 2026-09-20 05:11 UTC | 42m |
| IGO479 | IndiGo | Chennai International Airport (VOMM) | Mysore Airport (VOMY) | 2026-09-20 04:35 UTC | 2026-09-20 05:08 UTC | 33m |
| RYR5SB | Ryanair | Berlin Brandenburg Airport (EDDB) | Otocac Airport (LDRO) | 2026-09-20 04:01 UTC | 2026-09-20 05:08 UTC | 1h 6m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-09-20 04:43 UTC | 2026-09-20 05:07 UTC | 24m |
| EAF3777 | EAF | Sofia Airport (LBSF) | Antalya International Airport (LTAI) | 2026-09-20 03:44 UTC | 2026-09-20 05:07 UTC | 1h 23m |
| TRA119 | TRA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-09-20 04:49 UTC | 2026-09-20 05:07 UTC | 17m |
| IGO442 | IndiGo | Bengaluru International Airport (VOBL) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-20 02:46 UTC | 2026-09-20 05:06 UTC | 2h 20m |
| AIC116 | Air India | John F Kennedy International Airport (KJFK) | Pune Airport (VAPO) | 2026-09-19 15:17 UTC | 2026-09-20 05:05 UTC | 13h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
