# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_18:03:18_UTC-green)

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

**Latest saved flight:** 2026-08-20 18:03:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 18:03:18 UTC

- **220,089** saved flights
- **69,061** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,089** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,650,098.5 tonnes** estimated CO2 emissions
- **153,628,897 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8826 |
| 2 | SkyWest Airlines | 7841 |
| 3 | EJA | 4270 |
| 4 | IndiGo | 3732 |
| 5 | American Airlines | 3650 |
| 6 | Southwest Airlines | 3478 |
| 7 | Delta Air Lines | 2835 |
| 8 | ENY | 2711 |
| 9 | LATAM Airlines | 2090 |
| 10 | AZU | 2015 |
| 11 | Vueling | 1853 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1761 |
| 14 | LXJ | 1736 |
| 15 | easyJet | 1527 |
| 16 | Swiss International | 1465 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1384 |
| 19 | QLK | 1375 |
| 20 | EJU | 1372 |
| 21 | Alaska Airlines | 1341 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1202 |
| 24 | VIV | 1201 |
| 25 | Air France | 1195 |
| 26 | PGT | 1191 |
| 27 | WMT | 1160 |
| 28 | Wizz Air | 1122 |
| 29 | JetBlue | 1116 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185141 |
| 2 | 🇪🇸 ES | 14116 |
| 3 | 🇧🇷 BR | 12709 |
| 4 | 🇦🇺 AU | 12418 |
| 5 | 🇨🇦 CA | 12135 |
| 6 | 🇮🇹 IT | 11722 |
| 7 | 🇮🇳 IN | 11635 |
| 8 | 🇩🇪 DE | 10886 |
| 9 | 🇬🇧 GB | 10341 |
| 10 | 🇨🇴 CO | 9033 |
| 11 | 🇯🇵 JP | 8963 |
| 12 | 🇫🇷 FR | 8769 |
| 13 | 🇬🇷 GR | 6428 |
| 14 | 🇹🇷 TR | 6336 |
| 15 | 🇲🇽 MX | 6112 |
| 16 | 🇨🇭 CH | 5826 |
| 17 | 🇳🇴 NO | 5477 |
| 18 | 🇲🇾 MY | 3820 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3650 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2785 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2442 |
| 27 | 🇲🇦 MA | 2218 |
| 28 | 🇳🇱 NL | 1958 |
| 29 | 🇲🇪 ME | 1946 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4617 |
| 2 | Denver International Airport |  | US | 3590 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2668 |
| 5 | Guaymaral Airport |  | CO | 2600 |
| 6 | Harry Reid International Airport |  | US | 2422 |
| 7 | Zurich Airport |  | CH | 2287 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2257 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2237 |
| 10 | La Aurora Airport |  | GT | 2122 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2017 |
| 13 | Salt Lake City International Airport |  | US | 1940 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1904 |
| 15 | Congonhas Airport |  | BR | 1860 |
| 16 | Frankfurt am Main International Airport |  | DE | 1796 |
| 17 | Madrid Barajas International Airport |  | ES | 1728 |
| 18 | Capua Airport |  | IT | 1682 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1650 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1623 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1618 |
| 22 | Macau International Airport |  | MO | 1580 |
| 23 | Malpensa International Airport |  | IT | 1547 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1516 |
| 26 | Charlotte/Douglas International Airport |  | US | 1465 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1350 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1337 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1307 |
| 33 | Seattle-Tacoma International Airport |  | US | 1301 |
| 34 | Viracopos International Airport |  | BR | 1288 |
| 35 | Calgary International Airport |  | CA | 1240 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1223 |
| 37 | Oslo Gardermoen Airport |  | NO | 1222 |
| 38 | Vitoria/Foronda Airport |  | ES | 1222 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1182 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1062 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 789 | 21m | 244 km | 3,322.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 494 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 370 | 27m | 275 km | 1,753.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 322 | 44m | 241 km | 1,337.5 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 273 | 24m | 218 km | 1,028.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 259 | 1h 14m | 961 km | 4,293.1 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-20 16:29 UTC | 2026-08-20 18:03 UTC | 1h 33m |
| N75274 |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-20 17:37 UTC | 2026-08-20 18:03 UTC | 25m |
| FJO53F | FJO | London City Airport (EGLC) | Dublin Airport (EIDW) | 2026-08-20 17:01 UTC | 2026-08-20 17:58 UTC | 57m |
| N2103S |  | Montgomery-Gibbs Executive Airport (KMYF) | Big Bear City Airport (KL35) | 2026-08-20 17:09 UTC | 2026-08-20 17:47 UTC | 37m |
| N183TS |  | Nashville International Airport (KBNA) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-20 17:08 UTC | 2026-08-20 17:46 UTC | 38m |
| N480LF |  | Sunny Rest Airport (8PA8) | Lehigh Valley International Airport (KABE) | 2026-08-20 17:33 UTC | 2026-08-20 17:45 UTC | 11m |
| AAL1898 | American Airlines | Philadelphia International Airport (KPHL) | Key West International Airport (KEYW) | 2026-08-20 14:47 UTC | 2026-08-20 17:42 UTC | 2h 54m |
| N1218S |  | Rocky Mountain Metro Airport (KBJC) | Vance Brand Airport (KLMO) | 2026-08-20 16:19 UTC | 2026-08-20 17:39 UTC | 1h 19m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-20 16:00 UTC | 2026-08-20 17:36 UTC | 1h 36m |
| SL82 |  | Rota Naval Station Airport (LERT) | Gibraltar Airport (LXGB) | 2026-08-20 15:59 UTC | 2026-08-20 17:35 UTC | 1h 36m |
| N40EA |  | 22LL (22LL) | Skydive Chicago Airport (K8N2) | 2026-08-20 16:55 UTC | 2026-08-20 17:35 UTC | 39m |
| LXJ429 | LXJ | Chester County G O Carlson Airport (KMQS) | John F Kennedy International Airport (KJFK) | 2026-08-20 16:56 UTC | 2026-08-20 17:34 UTC | 38m |
| N892Z |  | Mc Mahon Field (68WA) | Scottsdale Airport (KSDL) | 2026-08-20 15:24 UTC | 2026-08-20 17:34 UTC | 2h 9m |
| RN047 |  | Skypark Estates Owners Assoc Airport (18FD) | Atmore Municipal Airport (K0R1) | 2026-08-20 17:19 UTC | 2026-08-20 17:33 UTC | 13m |
| WSN9 | WSN | Phoenix Sky Harbor International Airport (KPHX) | Lordsburg Municipal Airport (KLSB) | 2026-08-20 16:40 UTC | 2026-08-20 17:31 UTC | 51m |
| N668PD |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Los Alamitos Army Air Field (KSLI) | 2026-08-20 16:24 UTC | 2026-08-20 17:31 UTC | 1h 6m |
| DLH5CW | Lufthansa | Leipzig Halle Airport (EDDP) | Frankfurt am Main International Airport (EDDF) | 2026-08-20 16:54 UTC | 2026-08-20 17:29 UTC | 35m |
| N240VT |  | Scottsdale Airport (KSDL) | San Carlos Apache Airport (KP13) | 2026-08-20 17:06 UTC | 2026-08-20 17:29 UTC | 23m |
| DILIA | DIL | Hamburg Airport (EDDH) | Antwerp International Airport (Deurne) (EBAW) | 2026-08-20 16:25 UTC | 2026-08-20 17:29 UTC | 1h 3m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-20 17:12 UTC | 2026-08-20 17:28 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
