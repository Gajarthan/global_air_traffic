# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_08:20:07_UTC-green)

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

**Latest saved flight:** 2026-08-20 08:20:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 08:20:07 UTC

- **218,561** saved flights
- **68,764** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,561** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,630,432.7 tonnes** estimated CO2 emissions
- **152,488,854 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8753 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3710 |
| 5 | American Airlines | 3636 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2822 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2069 |
| 10 | AZU | 2002 |
| 11 | Vueling | 1834 |
| 12 | Lufthansa | 1814 |
| 13 | WIF | 1746 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1513 |
| 16 | Swiss International | 1455 |
| 17 | AXM | 1431 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1372 |
| 20 | EJU | 1361 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1317 |
| 23 | VIV | 1196 |
| 24 | GLO | 1187 |
| 25 | PGT | 1182 |
| 26 | Air France | 1180 |
| 27 | WMT | 1147 |
| 28 | JetBlue | 1112 |
| 29 | Wizz Air | 1109 |
| 30 | AEE | 1094 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184168 |
| 2 | 🇪🇸 ES | 13983 |
| 3 | 🇧🇷 BR | 12597 |
| 4 | 🇦🇺 AU | 12380 |
| 5 | 🇨🇦 CA | 12067 |
| 6 | 🇮🇹 IT | 11621 |
| 7 | 🇮🇳 IN | 11553 |
| 8 | 🇩🇪 DE | 10787 |
| 9 | 🇬🇧 GB | 10230 |
| 10 | 🇨🇴 CO | 8981 |
| 11 | 🇯🇵 JP | 8935 |
| 12 | 🇫🇷 FR | 8692 |
| 13 | 🇬🇷 GR | 6369 |
| 14 | 🇹🇷 TR | 6283 |
| 15 | 🇲🇽 MX | 6095 |
| 16 | 🇨🇭 CH | 5788 |
| 17 | 🇳🇴 NO | 5423 |
| 18 | 🇲🇾 MY | 3781 |
| 19 | 🇿🇦 ZA | 3705 |
| 20 | 🇵🇱 PL | 3612 |
| 21 | 🇹🇭 TH | 3599 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2945 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2627 |
| 26 | 🇭🇷 HR | 2398 |
| 27 | 🇲🇦 MA | 2195 |
| 28 | 🇳🇱 NL | 1941 |
| 29 | 🇲🇪 ME | 1918 |
| 30 | 🇮🇩 ID | 1852 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3576 |
| 3 | Tokyo International Airport |  | JP | 2684 |
| 4 | Indira Gandhi International Airport |  | IN | 2649 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2267 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2221 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1780 |
| 17 | Madrid Barajas International Airport |  | ES | 1711 |
| 18 | Capua Airport |  | IT | 1664 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1618 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1604 |
| 22 | Macau International Airport |  | MO | 1566 |
| 23 | Malpensa International Airport |  | IT | 1540 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1538 |
| 25 | Charles de Gaulle International Airport |  | FR | 1496 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1399 |
| 28 | Kuala Lumpur International Airport |  | MY | 1389 |
| 29 | Barcelona International Airport |  | ES | 1338 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1319 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1278 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1209 |
| 37 | Vitoria/Foronda Airport |  | ES | 1209 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1189 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1174 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 785 | 21m | 244 km | 3,305.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 541 | 1h 7m | 770 km | 7,186.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 519 | 24m | 225 km | 2,013.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 366 | 27m | 275 km | 1,734.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 321 | 1h 50m | 1,423 km | 7,877.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 319 | 44m | 241 km | 1,325.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 286 | 21m | 250 km | 1,235.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 270 | 24m | 218 km | 1,017.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 268 | 27m | 215 km | 992.6 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 248 | 19m | 144 km | 616.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 242 | 44m | 555 km | 2,317.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKRTK | OKR | Plzen Line Airport (LKLN) | Mlada Boleslav Airport (LKMB) | 2026-08-20 06:37 UTC | 2026-08-20 08:20 UTC | 1h 42m |
| SUNDOG1 | SUN | Nordholz Airport (ETMN) | Bopfingen Airport (EDNQ) | 2026-08-20 07:21 UTC | 2026-08-20 08:07 UTC | 45m |
| OKLHE | OKL | Hradec Kralove Airport (LKHK) | Ostrava Leos Janacek Airport (LKMT) | 2026-08-20 07:08 UTC | 2026-08-20 08:05 UTC | 56m |
| CJT570 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Montréal (Mirabel) Airport (CYMX) | 2026-08-20 05:56 UTC | 2026-08-20 08:05 UTC | 2h 8m |
| EFC23E | EFC | Al Maktoum International Airport (OMDW) | Al Saqr Field (OMRS) | 2026-08-20 07:06 UTC | 2026-08-20 08:02 UTC | 56m |
| MAI333 | MAI | LRPV (LRPV) | LRPV (LRPV) | 2026-08-20 07:03 UTC | 2026-08-20 07:55 UTC | 52m |
| FD258 |  | Hamilton Airport (YHML) | Wycheproof Airport (YWYF) | 2026-08-20 07:31 UTC | 2026-08-20 07:55 UTC | 24m |
| ICY52 | ICY | Highland Airport (47AK) | Elmendorf Afb Airport (PAED) | 2026-08-20 07:10 UTC | 2026-08-20 07:49 UTC | 39m |
| EAI7S | EAI | Dublin Airport (EIDW) | Southampton Airport (EGHI) | 2026-08-20 06:35 UTC | 2026-08-20 07:48 UTC | 1h 12m |
| FNY55D5 | FNY | Landivisiau Air Base (LFRJ) | La Roche-sur-Yon Airport (LFRI) | 2026-08-20 07:17 UTC | 2026-08-20 07:41 UTC | 24m |
| PR24 |  | Karup Airport (EKKA) | Billund Airport (EKBI) | 2026-08-20 07:18 UTC | 2026-08-20 07:41 UTC | 22m |
| SAS38H | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Eleftherios Venizelos International Airport (LGAV) | 2026-08-20 04:12 UTC | 2026-08-20 07:40 UTC | 3h 28m |
| SEH2JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-20 07:07 UTC | 2026-08-20 07:40 UTC | 32m |
| RYR90QC | Ryanair | Brussels South Charleroi Airport (EBCI) | Manchester Airport (EGCC) | 2026-08-20 06:43 UTC | 2026-08-20 07:40 UTC | 56m |
| EOK5133 | EOK | Cheongju International Airport (RKTU) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-20 05:26 UTC | 2026-08-20 07:40 UTC | 2h 13m |
| OMS762 | OMS | Juhu Aerodrome (VAJJ) | Saiq Airport (OOSQ) | 2026-08-20 00:20 UTC | 2026-08-20 07:39 UTC | 7h 19m |
| RYR23YL | Ryanair | Gothenburg-Landvetter Airport (ESGG) | Stapleford Aerodrome (EGSG) | 2026-08-20 05:57 UTC | 2026-08-20 07:38 UTC | 1h 41m |
| VOE3607 | VOE | Alhama De Murcia Airport (LELH) | La Morgal Airport (LEMR) | 2026-08-20 06:33 UTC | 2026-08-20 07:38 UTC | 1h 5m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-08-20 07:17 UTC | 2026-08-20 07:37 UTC | 20m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-20 07:14 UTC | 2026-08-20 07:37 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
