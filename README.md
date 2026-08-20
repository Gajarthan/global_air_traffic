# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_22:27:33_UTC-green)

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

**Latest saved flight:** 2026-08-20 22:27:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 22:27:33 UTC

- **220,605** saved flights
- **69,217** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,605** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,655,763.0 tonnes** estimated CO2 emissions
- **153,957,273 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8841 |
| 2 | SkyWest Airlines | 7874 |
| 3 | EJA | 4282 |
| 4 | IndiGo | 3732 |
| 5 | American Airlines | 3659 |
| 6 | Southwest Airlines | 3485 |
| 7 | Delta Air Lines | 2842 |
| 8 | ENY | 2718 |
| 9 | LATAM Airlines | 2097 |
| 10 | AZU | 2021 |
| 11 | Vueling | 1858 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1744 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1390 |
| 19 | QLK | 1376 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1345 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1206 |
| 24 | VIV | 1203 |
| 25 | Air France | 1196 |
| 26 | PGT | 1196 |
| 27 | WMT | 1163 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1116 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185745 |
| 2 | 🇪🇸 ES | 14136 |
| 3 | 🇧🇷 BR | 12745 |
| 4 | 🇦🇺 AU | 12425 |
| 5 | 🇨🇦 CA | 12179 |
| 6 | 🇮🇹 IT | 11738 |
| 7 | 🇮🇳 IN | 11637 |
| 8 | 🇩🇪 DE | 10893 |
| 9 | 🇬🇧 GB | 10365 |
| 10 | 🇨🇴 CO | 9069 |
| 11 | 🇯🇵 JP | 8963 |
| 12 | 🇫🇷 FR | 8782 |
| 13 | 🇬🇷 GR | 6436 |
| 14 | 🇹🇷 TR | 6351 |
| 15 | 🇲🇽 MX | 6130 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3820 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇵🇱 PL | 3661 |
| 21 | 🇹🇭 TH | 3655 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2963 |
| 24 | 🇬🇹 GT | 2787 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2446 |
| 27 | 🇲🇦 MA | 2219 |
| 28 | 🇳🇱 NL | 1962 |
| 29 | 🇲🇪 ME | 1950 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4631 |
| 2 | Denver International Airport |  | US | 3606 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2668 |
| 5 | Guaymaral Airport |  | CO | 2604 |
| 6 | Harry Reid International Airport |  | US | 2427 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2268 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2240 |
| 10 | La Aurora Airport |  | GT | 2123 |
| 11 | El Dorado International Airport |  | CO | 2064 |
| 12 | Chicago O'Hare International Airport |  | US | 2023 |
| 13 | Salt Lake City International Airport |  | US | 1943 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1907 |
| 15 | Congonhas Airport |  | BR | 1866 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1657 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1624 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1624 |
| 22 | Macau International Airport |  | MO | 1583 |
| 23 | Malpensa International Airport |  | IT | 1548 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1518 |
| 26 | Charlotte/Douglas International Airport |  | US | 1468 |
| 27 | Ninoy Aquino International Airport |  | PH | 1409 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1353 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1338 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1312 |
| 33 | Seattle-Tacoma International Airport |  | US | 1305 |
| 34 | Viracopos International Airport |  | BR | 1292 |
| 35 | Calgary International Airport |  | CA | 1246 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1063 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 791 | 21m | 244 km | 3,330.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 274 | 24m | 218 km | 1,032.3 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 249 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ES801 |  | Sacramento Mather Airport (KMHR) | Castle Airport (KMER) | 2026-08-20 21:38 UTC | 2026-08-20 22:27 UTC | 48m |
| N282MM |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-20 21:46 UTC | 2026-08-20 22:27 UTC | 40m |
| AUB111 | AUB | Auburn University Regional Airport (KAUO) | Grayhill Airport (GA98) | 2026-08-20 21:49 UTC | 2026-08-20 22:26 UTC | 37m |
| EZY47HB | easyJet | Copenhagen Kastrup Airport (EKCH) | Bristol International Airport (EGGD) | 2026-08-20 20:33 UTC | 2026-08-20 22:22 UTC | 1h 48m |
| AAL2832 | American Airlines | Okc Will Rogers International Airport (KOKC) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-20 21:49 UTC | 2026-08-20 22:20 UTC | 31m |
| N440AT |  | Rantoul Ntl Avn Cntr-Frank Elliott Field (KTIP) | Niklaus Airport (IS26) | 2026-08-20 21:45 UTC | 2026-08-20 22:17 UTC | 32m |
| FLC78 | FLC | Chloride Airport (NM51) | Rancho Magdalena Airport (NM01) | 2026-08-20 20:39 UTC | 2026-08-20 22:16 UTC | 1h 36m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-20 21:35 UTC | 2026-08-20 22:15 UTC | 40m |
| AWH95A | AWH | Hannover Airport (EDDV) | Leipzig Halle Airport (EDDP) | 2026-08-20 21:46 UTC | 2026-08-20 22:14 UTC | 28m |
| CXK404 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-08-20 20:56 UTC | 2026-08-20 22:14 UTC | 1h 17m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-20 21:57 UTC | 2026-08-20 22:14 UTC | 16m |
| CNS117 | CNS | New Kent County Airport (KW96) | Lebanon Municipal Airport (KLEB) | 2026-08-20 21:02 UTC | 2026-08-20 22:13 UTC | 1h 10m |
| N5399K |  | Bolingbrook's Clow International Airport (K1C5) | Morris Municipal/James R Washburn Field (KC09) | 2026-08-20 21:41 UTC | 2026-08-20 22:10 UTC | 29m |
| DTCHMN42 | DTC | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-20 21:52 UTC | 2026-08-20 22:03 UTC | 11m |
| N499MD |  | Flying Cloud Airport (KFCM) | Glendale Regional Airport (KGEU) | 2026-08-20 19:11 UTC | 2026-08-20 22:01 UTC | 2h 50m |
| N36GV |  | El Paso International Airport (KELP) | Stovall Ranch Nr 4 Airport (6TX9) | 2026-08-20 15:19 UTC | 2026-08-20 21:58 UTC | 6h 39m |
| N8823W |  | Petaluma Municipal Airport (KO69) | Sacramento Mather Airport (KMHR) | 2026-08-20 21:18 UTC | 2026-08-20 21:58 UTC | 40m |
| EFY7816 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-08-20 21:27 UTC | 2026-08-20 21:55 UTC | 27m |
| N51HF |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-08-20 21:24 UTC | 2026-08-20 21:54 UTC | 29m |
| N29BY |  | KU77 (KU77) | Provo Municipal Airport (KPVU) | 2026-08-20 21:48 UTC | 2026-08-20 21:53 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
