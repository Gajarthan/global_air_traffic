# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_22:12:55_UTC-green)

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

**Latest saved flight:** 2026-09-02 22:12:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-02 22:12:55 UTC

- **245,283** saved flights
- **74,131** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **245,283** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,954,693.2 tonnes** estimated CO2 emissions
- **171,286,562 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9844 |
| 2 | SkyWest Airlines | 8585 |
| 3 | EJA | 4732 |
| 4 | IndiGo | 4104 |
| 5 | American Airlines | 3941 |
| 6 | Southwest Airlines | 3675 |
| 7 | Delta Air Lines | 3119 |
| 8 | ENY | 2942 |
| 9 | LATAM Airlines | 2356 |
| 10 | AZU | 2281 |
| 11 | Vueling | 2100 |
| 12 | Lufthansa | 1962 |
| 13 | WIF | 1961 |
| 14 | LXJ | 1895 |
| 15 | easyJet | 1705 |
| 16 | Swiss International | 1654 |
| 17 | AXM | 1613 |
| 18 | EJU | 1580 |
| 19 | QLK | 1569 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1465 |
| 22 | All Nippon Airways | 1443 |
| 23 | WMT | 1383 |
| 24 | GLO | 1370 |
| 25 | PGT | 1344 |
| 26 | Air France | 1342 |
| 27 | VIV | 1342 |
| 28 | Wizz Air | 1329 |
| 29 | AEE | 1210 |
| 30 | JetBlue | 1209 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203219 |
| 2 | 🇪🇸 ES | 15751 |
| 3 | 🇧🇷 BR | 14304 |
| 4 | 🇦🇺 AU | 13931 |
| 5 | 🇨🇦 CA | 13653 |
| 6 | 🇮🇹 IT | 13450 |
| 7 | 🇮🇳 IN | 12797 |
| 8 | 🇩🇪 DE | 12100 |
| 9 | 🇬🇧 GB | 11565 |
| 10 | 🇨🇴 CO | 10647 |
| 11 | 🇫🇷 FR | 9904 |
| 12 | 🇯🇵 JP | 9751 |
| 13 | 🇹🇷 TR | 7297 |
| 14 | 🇬🇷 GR | 7233 |
| 15 | 🇲🇽 MX | 6765 |
| 16 | 🇨🇭 CH | 6593 |
| 17 | 🇳🇴 NO | 6088 |
| 18 | 🇹🇭 TH | 4429 |
| 19 | 🇲🇾 MY | 4324 |
| 20 | 🇿🇦 ZA | 4259 |
| 21 | 🇵🇱 PL | 4118 |
| 22 | 🇳🇿 NZ | 3360 |
| 23 | 🇵🇭 PH | 3356 |
| 24 | 🇬🇹 GT | 3073 |
| 25 | 🇰🇷 KR | 2870 |
| 26 | 🇭🇷 HR | 2825 |
| 27 | 🇲🇦 MA | 2479 |
| 28 | 🇲🇪 ME | 2296 |
| 29 | 🇳🇱 NL | 2220 |
| 30 | 🇮🇩 ID | 2137 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5053 |
| 2 | Denver International Airport |  | US | 3956 |
| 3 | Indira Gandhi International Airport |  | IN | 2986 |
| 4 | Tokyo International Airport |  | JP | 2906 |
| 5 | Guaymaral Airport |  | CO | 2718 |
| 6 | Harry Reid International Airport |  | US | 2612 |
| 7 | Zurich Airport |  | CH | 2577 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2495 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2442 |
| 10 | El Dorado International Airport |  | CO | 2423 |
| 11 | La Aurora Airport |  | GT | 2338 |
| 12 | Salt Lake City International Airport |  | US | 2172 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2096 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2026 |
| 16 | Frankfurt am Main International Airport |  | DE | 1933 |
| 17 | Capua Airport |  | IT | 1929 |
| 18 | Madrid Barajas International Airport |  | ES | 1927 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1844 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1803 |
| 21 | Malpensa International Airport |  | IT | 1757 |
| 22 | Charles de Gaulle International Airport |  | FR | 1727 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 1724 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1715 |
| 25 | Ninoy Aquino International Airport |  | PH | 1634 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1588 |
| 28 | Charlotte/Douglas International Airport |  | US | 1564 |
| 29 | Kuala Lumpur International Airport |  | MY | 1558 |
| 30 | Barcelona International Airport |  | ES | 1552 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1488 |
| 32 | Viracopos International Airport |  | BR | 1457 |
| 33 | Seattle-Tacoma International Airport |  | US | 1440 |
| 34 | Don Mueang International Airport |  | TH | 1424 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1421 |
| 36 | Bengaluru International Airport |  | IN | 1416 |
| 37 | Calgary International Airport |  | CA | 1411 |
| 38 | Oslo Gardermoen Airport |  | NO | 1383 |
| 39 | Vancouver International Airport |  | CA | 1366 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 907 | 21m | 244 km | 3,819.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 638 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 624 | 24m | 225 km | 2,420.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 550 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 387 | 1h 50m | 1,423 km | 9,497.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 376 | 44m | 555 km | 3,600.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 348 | 21m | 250 km | 1,503.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 337 | 24m | 218 km | 1,269.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 328 | 1h 39m | 1,156 km | 6,543.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 300 | 27m | 215 km | 1,111.1 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 283 | 1h 14m | 961 km | 4,690.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 278 | 19m | 144 km | 691.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 264 | 1h 50m | 1,304 km | 5,939.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8168 |  | Van Nuys Airport (KVNY) | Lake Tahoe Airport (KTVL) | 2026-09-02 21:29 UTC | 2026-09-02 22:12 UTC | 43m |
| N1377E |  | Appleton International Airport (KATW) | M & F Landing Airport (WI52) | 2026-09-02 21:24 UTC | 2026-09-02 22:11 UTC | 47m |
| RYR12KH | Ryanair | Malaga Airport (LEMG) | Dublin Airport (EIDW) | 2026-09-02 19:35 UTC | 2026-09-02 22:10 UTC | 2h 34m |
| N33RK |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-09-02 21:24 UTC | 2026-09-02 21:59 UTC | 34m |
| SRR7993 | SRR | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Leipzig Halle Airport (EDDP) | 2026-09-02 20:45 UTC | 2026-09-02 21:56 UTC | 1h 10m |
| NIT258 | NIT | Heart Of Georgia Regional Airport (KEZM) | Heart Of Georgia Regional Airport (KEZM) | 2026-09-02 20:01 UTC | 2026-09-02 21:55 UTC | 1h 54m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-02 20:32 UTC | 2026-09-02 21:55 UTC | 1h 23m |
| N497MT |  | Dupage Airport (KDPA) | Central Il Regional/Bloomington-Normal Airport (KBMI) | 2026-09-02 21:18 UTC | 2026-09-02 21:53 UTC | 34m |
| N923JK |  | Waukesha County Airport (KUES) | Miller-Herrold Airport (28MI) | 2026-09-02 21:18 UTC | 2026-09-02 21:53 UTC | 35m |
| N65JA |  | Aurora Municipal Airport (KARR) | Woodlake Landing Airport (IS65) | 2026-09-02 21:25 UTC | 2026-09-02 21:53 UTC | 27m |
| N889MR |  | Laredo International Airport (KLRD) | Phoenix Sky Harbor International Airport (KPHX) | 2026-09-02 19:59 UTC | 2026-09-02 21:52 UTC | 1h 53m |
| N917JG |  | Modesto City-County-Harry Sham Field (KMOD) | Palm Springs International Airport (KPSP) | 2026-09-02 20:31 UTC | 2026-09-02 21:50 UTC | 1h 18m |
| XBNLT | XBN | Hermanos Serdan International Airport (MMPB) | Atizapan De Zaragoza Airport (MMJC) | 2026-09-02 20:55 UTC | 2026-09-02 21:48 UTC | 53m |
| N41GA |  | Rogue Valley International/Medford Airport (KMFR) | Siskiyou County Airport (KSIY) | 2026-09-02 21:33 UTC | 2026-09-02 21:47 UTC | 14m |
| EFY7838 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-02 21:17 UTC | 2026-09-02 21:46 UTC | 29m |
| ARCAS31 | ARC | Danaher Airport (7TX0) | Arledge Field (KF56) | 2026-09-02 21:35 UTC | 2026-09-02 21:46 UTC | 11m |
| N439H |  | Bradley International Airport (KBDL) | Laguardia Airport (KLGA) | 2026-09-02 20:34 UTC | 2026-09-02 21:46 UTC | 1h 11m |
| N980CE |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-09-02 21:11 UTC | 2026-09-02 21:45 UTC | 33m |
| COBRA31 | COB | Boron Airstrip (57CL) | Boron Airstrip (57CL) | 2026-09-02 20:57 UTC | 2026-09-02 21:44 UTC | 47m |
| EJA892 | EJA | Kansas City Downtown/Wheeler Field (KMKC) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-02 20:27 UTC | 2026-09-02 21:42 UTC | 1h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
