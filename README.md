# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_09:35:09_UTC-green)

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

**Latest saved flight:** 2026-08-22 09:35:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 09:35:09 UTC

- **225,070** saved flights
- **70,092** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,070** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,711,168.9 tonnes** estimated CO2 emissions
- **157,169,213 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9023 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3802 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2140 |
| 10 | AZU | 2074 |
| 11 | Vueling | 1899 |
| 12 | Lufthansa | 1850 |
| 13 | WIF | 1789 |
| 14 | LXJ | 1777 |
| 15 | easyJet | 1556 |
| 16 | Swiss International | 1496 |
| 17 | AXM | 1486 |
| 18 | QLK | 1420 |
| 19 | United Airlines | 1417 |
| 20 | EJU | 1416 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1350 |
| 23 | GLO | 1244 |
| 24 | PGT | 1236 |
| 25 | VIV | 1231 |
| 26 | Air France | 1222 |
| 27 | WMT | 1201 |
| 28 | Wizz Air | 1158 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1121 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188730 |
| 2 | 🇪🇸 ES | 14407 |
| 3 | 🇧🇷 BR | 13053 |
| 4 | 🇦🇺 AU | 12770 |
| 5 | 🇨🇦 CA | 12480 |
| 6 | 🇮🇹 IT | 12045 |
| 7 | 🇮🇳 IN | 11855 |
| 8 | 🇩🇪 DE | 11080 |
| 9 | 🇬🇧 GB | 10543 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9163 |
| 12 | 🇫🇷 FR | 8978 |
| 13 | 🇹🇷 TR | 6575 |
| 14 | 🇬🇷 GR | 6565 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5923 |
| 17 | 🇳🇴 NO | 5568 |
| 18 | 🇲🇾 MY | 3957 |
| 19 | 🇿🇦 ZA | 3885 |
| 20 | 🇹🇭 TH | 3846 |
| 21 | 🇵🇱 PL | 3728 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3072 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2673 |
| 26 | 🇭🇷 HR | 2523 |
| 27 | 🇲🇦 MA | 2262 |
| 28 | 🇲🇪 ME | 2005 |
| 29 | 🇳🇱 NL | 2001 |
| 30 | 🇮🇩 ID | 1940 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2739 |
| 4 | Indira Gandhi International Airport |  | IN | 2731 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2331 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2275 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1816 |
| 17 | Madrid Barajas International Airport |  | ES | 1758 |
| 18 | Capua Airport |  | IT | 1729 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1678 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1667 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1592 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1587 |
| 24 | Malpensa International Airport |  | IT | 1579 |
| 25 | Charles de Gaulle International Airport |  | FR | 1556 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1468 |
| 28 | Kuala Lumpur International Airport |  | MY | 1439 |
| 29 | Barcelona International Airport |  | ES | 1390 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1341 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1323 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1264 |
| 38 | Oslo Gardermoen Airport |  | NO | 1254 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1214 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 560 | 1h 7m | 770 km | 7,439.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 554 | 24m | 225 km | 2,149.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 338 | 1h 50m | 1,423 km | 8,295.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 327 | 44m | 241 km | 1,358.3 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 17 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 285 | 44m | 555 km | 2,729.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 283 | 24m | 218 km | 1,066.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 257 | 19m | 144 km | 639.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GGWMB | GGW | Turweston Airport (EGBT) | Turweston Airport (EGBT) | 2026-08-22 08:04 UTC | 2026-08-22 09:35 UTC | 1h 30m |
| SIO619 | SIO | Rimini / Miramare - Federico Fellini International Airport (LIPR) | Samedan Airport (LSZS) | 2026-08-22 08:35 UTC | 2026-08-22 09:17 UTC | 42m |
| OKCUN20 | OKC | Brno-Turany Airport (LKTB) | Brno-Turany Airport (LKTB) | 2026-08-22 08:13 UTC | 2026-08-22 09:14 UTC | 1h 1m |
| PH712 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-08-22 08:48 UTC | 2026-08-22 08:56 UTC | 8m |
| AXM6082 | AXM | Senai International Airport (WMKJ) | Jendarata Airport (WMAJ) | 2026-08-22 08:21 UTC | 2026-08-22 08:56 UTC | 35m |
| FXJ69N | FXJ | Geneva Cointrin International Airport (LSGG) | Cannes-Mandelieu Airport (LFMD) | 2026-08-22 08:08 UTC | 2026-08-22 08:55 UTC | 46m |
| N1065B |  | Hartsfield/Jackson Atlanta International Airport (KATL) | John F Kennedy International Airport (KJFK) | 2026-08-22 05:16 UTC | 2026-08-22 08:54 UTC | 3h 38m |
| AWA475 | AWA | VGZR (VGZR) | VGBG (VGBG) | 2026-08-22 08:23 UTC | 2026-08-22 08:54 UTC | 31m |
| RYR4957 | Ryanair | Valencia Airport (LEVC) | Bassatine Airport (GMFM) | 2026-08-22 07:53 UTC | 2026-08-22 08:54 UTC | 1h 1m |
| AIQ3306 | AIQ | Don Mueang International Airport (VTBD) | Takhli Airport (VTPI) | 2026-08-22 08:36 UTC | 2026-08-22 08:53 UTC | 17m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-22 08:28 UTC | 2026-08-22 08:51 UTC | 22m |
| JAL2825 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-08-22 08:07 UTC | 2026-08-22 08:50 UTC | 43m |
| FAD810 | FAD | Kutahya Airport (LTBN) | Abqaiq Airport (OEBQ) | 2026-08-22 02:30 UTC | 2026-08-22 08:41 UTC | 6h 10m |
| WMT1097 | WMT | Ciampino Airport (LIRA) | Corte Airport (LFKT) | 2026-08-22 08:12 UTC | 2026-08-22 08:38 UTC | 25m |
| EXS419 | EXS | Leeds Bradford Airport (EGNM) | Menorca Airport (LEMH) | 2026-08-22 06:21 UTC | 2026-08-22 08:35 UTC | 2h 13m |
| DAL2186 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Fairbanks International Airport (PAFA) | 2026-08-22 05:26 UTC | 2026-08-22 08:33 UTC | 3h 7m |
| SUBTR | SUB | October Airport (HEOC) | HE30 (HE30) | 2026-08-22 07:57 UTC | 2026-08-22 08:33 UTC | 36m |
| VCG1BG | VCG | Bournemouth Airport (EGHH) | Raron Airport (LSTA) | 2026-08-22 07:10 UTC | 2026-08-22 08:31 UTC | 1h 21m |
| WUK4ZE | WUK | London Luton Airport (EGGW) | Visoko Sport Airfield (LQVI) | 2026-08-22 06:34 UTC | 2026-08-22 08:30 UTC | 1h 55m |
| KLM23L | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Capua Airport (LIAU) | 2026-08-22 06:43 UTC | 2026-08-22 08:30 UTC | 1h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
