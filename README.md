# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_23:24:20_UTC-green)

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

**Latest saved flight:** 2026-07-24 23:24:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 23:24:20 UTC

- **149,147** saved flights
- **49,743** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,147** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,784,033.2 tonnes** estimated CO2 emissions
- **103,422,216 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6015 |
| 2 | SkyWest Airlines | 5465 |
| 3 | EJA | 2960 |
| 4 | IndiGo | 2666 |
| 5 | American Airlines | 2375 |
| 6 | Southwest Airlines | 2262 |
| 7 | ENY | 1859 |
| 8 | Delta Air Lines | 1760 |
| 9 | Lufthansa | 1455 |
| 10 | LATAM Airlines | 1375 |
| 11 | AZU | 1289 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1258 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 965 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 933 |
| 20 | QLK | 922 |
| 21 | EJU | 910 |
| 22 | VIV | 823 |
| 23 | CXK | 799 |
| 24 | AEE | 781 |
| 25 | JetBlue | 780 |
| 26 | Air France | 779 |
| 27 | Cathay Pacific | 779 |
| 28 | MXY | 777 |
| 29 | GLO | 772 |
| 30 | United Airlines | 771 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 128898 |
| 2 | 🇪🇸 ES | 9616 |
| 3 | 🇦🇺 AU | 8463 |
| 4 | 🇧🇷 BR | 8419 |
| 5 | 🇮🇳 IN | 8374 |
| 6 | 🇨🇦 CA | 8003 |
| 7 | 🇮🇹 IT | 7704 |
| 8 | 🇩🇪 DE | 7616 |
| 9 | 🇬🇧 GB | 6814 |
| 10 | 🇯🇵 JP | 6156 |
| 11 | 🇫🇷 FR | 5904 |
| 12 | 🇨🇴 CO | 5030 |
| 13 | 🇲🇽 MX | 4324 |
| 14 | 🇬🇷 GR | 4214 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3899 |
| 17 | 🇹🇷 TR | 3502 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2510 |
| 20 | 🇿🇦 ZA | 2406 |
| 21 | 🇳🇿 NZ | 2253 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2056 |
| 24 | 🇵🇭 PH | 1979 |
| 25 | 🇬🇹 GT | 1947 |
| 26 | 🇲🇦 MA | 1522 |
| 27 | 🇲🇪 ME | 1470 |
| 28 | 🇳🇱 NL | 1380 |
| 29 | 🇭🇷 HR | 1353 |
| 30 | 🇲🇴 MO | 1242 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3071 |
| 2 | Denver International Airport |  | US | 2507 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Guaymaral Airport |  | CO | 1866 |
| 5 | Indira Gandhi International Airport |  | IN | 1860 |
| 6 | Harry Reid International Airport |  | US | 1852 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1669 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1572 |
| 10 | La Aurora Airport |  | GT | 1508 |
| 11 | Frankfurt am Main International Airport |  | DE | 1405 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1402 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1344 |
| 15 | El Dorado International Airport |  | CO | 1342 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1282 |
| 17 | Macau International Airport |  | MO | 1242 |
| 18 | Congonhas Airport |  | BR | 1203 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1182 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1158 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1067 |
| 24 | Charlotte/Douglas International Airport |  | US | 1064 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1049 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1002 |
| 28 | Malpensa International Airport |  | IT | 964 |
| 29 | Ninoy Aquino International Airport |  | PH | 927 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 908 |
| 31 | Barcelona International Airport |  | ES | 898 |
| 32 | Daniel K Inouye International Airport |  | US | 895 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 893 |
| 34 | Seattle-Tacoma International Airport |  | US | 858 |
| 35 | Calgary International Airport |  | CA | 853 |
| 36 | Tenerife Norte Airport |  | ES | 852 |
| 37 | Scottsdale Airport |  | US | 847 |
| 38 | Viracopos International Airport |  | BR | 841 |
| 39 | Amsterdam Airport Schiphol |  | NL | 830 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 787 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 541 | 21m | 244 km | 2,278.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 269 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 266 | 27m | 275 km | 1,260.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 203 | 44m | 241 km | 843.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 196 | 20m | 99 km | 335.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 183 | 20m | 250 km | 790.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 176 | 31m | 369 km | 1,120.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LS04 |  | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-24 22:55 UTC | 2026-07-24 23:24 UTC | 29m |
| N82769 |  | Bear Cove Farm Airport (46AK) | Bear Cove Farm Airport (46AK) | 2026-07-24 22:44 UTC | 2026-07-24 23:22 UTC | 37m |
| RNGR776 | RNG | Victoria Regional Airport (KVCT) | XS10 (XS10) | 2026-07-24 22:49 UTC | 2026-07-24 23:20 UTC | 31m |
| N9939Z |  | King Salmon Airport (PAKN) | King Salmon Airport (PAKN) | 2026-07-24 23:04 UTC | 2026-07-24 23:19 UTC | 14m |
| N505XX |  | KU77 (KU77) | KU77 (KU77) | 2026-07-24 22:57 UTC | 2026-07-24 23:15 UTC | 18m |
| VTM599 | VTM | Cincinnati/Northern Kentucky International Airport (KCVG) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-07-24 22:43 UTC | 2026-07-24 23:14 UTC | 31m |
| CFGVS | CFG | Abbotsford Airport (CYXX) | Abbotsford Airport (CYXX) | 2026-07-24 22:15 UTC | 2026-07-24 23:12 UTC | 57m |
| N587BA |  | Green Mountain Airport (WA67) | WN10 (WN10) | 2026-07-24 22:53 UTC | 2026-07-24 23:11 UTC | 18m |
| CLX4325 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-07-24 12:25 UTC | 2026-07-24 23:09 UTC | 10h 44m |
| GRA523 | GRA | Tobias Bolanos International Airport (MRPV) | Juan Santamaria International Airport (MROC) | 2026-07-24 22:55 UTC | 2026-07-24 23:05 UTC | 10m |
| TGGMP | TGG | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-07-24 22:44 UTC | 2026-07-24 23:02 UTC | 18m |
| N500KB |  | Frederick Municipal Airport (KFDK) | Ocean City Municipal Airport (KOXB) | 2026-07-24 22:14 UTC | 2026-07-24 23:00 UTC | 46m |
| N8452R |  | Saginaw County/H W Browne Airport (KHYX) | Saginaw County/H W Browne Airport (KHYX) | 2026-07-24 22:49 UTC | 2026-07-24 23:00 UTC | 10m |
| N717AF |  | Christensen Ranch Airport (9CL2) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-24 22:47 UTC | 2026-07-24 22:59 UTC | 12m |
| N88JA |  | Dayton/Wright Brothers Airport (KMGY) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-24 22:32 UTC | 2026-07-24 22:59 UTC | 26m |
| TKR183 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-07-24 22:48 UTC | 2026-07-24 22:58 UTC | 10m |
| N545CW |  | Easton State Airport (KESW) | Renton Municipal Airport (KRNT) | 2026-07-24 22:15 UTC | 2026-07-24 22:56 UTC | 41m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-07-24 07:12 UTC | 2026-07-24 22:54 UTC | 15h 42m |
| N9824V |  | Olympia Regional Airport (KOLM) | WN24 (WN24) | 2026-07-24 22:24 UTC | 2026-07-24 22:52 UTC | 28m |
| N578JZ |  | Gansner Field (K2O1) | Hayfork Airport (KF62) | 2026-07-24 22:23 UTC | 2026-07-24 22:52 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
